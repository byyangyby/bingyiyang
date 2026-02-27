#!/usr/bin/env python3
"""
Fetch DOI and PMID for all entries in papers.bib using PubMed E-utilities API.
Also fetches Google Scholar citation IDs from the user's profile.
Updates papers.bib in place with the found metadata.
"""
import re
import json
import time
import urllib.request
import urllib.parse
import sys

BIB_FILE = "/Users/bingyiyang/Documents/GitHub/bingyiyang/_bibliography/papers.bib"
SCHOLAR_USER_ID = "1IQInjgAAAAJ"


def parse_bib_entries(content):
    """Parse bib file into list of (key, entry_text, title, year, doi) tuples."""
    # Split on @article{ patterns
    entries = []
    # Match each @article{key, ... } block
    pattern = re.compile(r'(@article\{([^,]+),\s*\n(.*?))\n\}', re.DOTALL)
    for match in pattern.finditer(content):
        full_match = match.group(0)
        key = match.group(2).strip()
        body = match.group(3)
        
        # Extract title
        title_match = re.search(r'title\s*=\s*\{([^}]+)\}', body)
        title = title_match.group(1) if title_match else ""
        
        # Extract year
        year_match = re.search(r'year\s*=\s*\{(\d+)\}', body)
        year = year_match.group(1) if year_match else ""
        
        # Extract existing doi
        doi_match = re.search(r'doi\s*=\s*\{([^}]+)\}', body)
        doi = doi_match.group(1) if doi_match else ""
        
        # Extract first author last name
        author_match = re.search(r'author\s*=\s*\{([^,]+)', body)
        first_author = author_match.group(1).strip() if author_match else ""
        
        entries.append({
            'key': key,
            'title': title,
            'year': year,
            'doi': doi,
            'first_author': first_author,
        })
    return entries


def search_pubmed(title, first_author="", year=""):
    """Search PubMed for a paper by title. Returns (pmid, doi) or (None, None)."""
    # Clean title for search
    clean_title = re.sub(r'[{}\\\'"]', '', title)
    clean_title = re.sub(r'\s+', ' ', clean_title).strip()
    
    # Build search query
    query = f'{clean_title}[Title]'
    
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=3&term={urllib.parse.quote(query)}'
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
        
        id_list = data.get('esearchresult', {}).get('idlist', [])
        if not id_list:
            return None, None
        
        pmid = id_list[0]
        
        # Fetch details to get DOI
        detail_url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json'
        req2 = urllib.request.Request(detail_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req2, timeout=10) as resp2:
            detail_data = json.loads(resp2.read().decode())
        
        result = detail_data.get('result', {}).get(pmid, {})
        doi = ""
        for aid in result.get('articleids', []):
            if aid.get('idtype') == 'doi':
                doi = aid.get('value', '')
                break
        
        return pmid, doi
    except Exception as e:
        print(f"  Error searching PubMed: {e}", file=sys.stderr)
        return None, None


def search_crossref(title):
    """Search CrossRef for a paper by title. Returns doi or None."""
    clean_title = re.sub(r'[{}\\\'"]', '', title)
    clean_title = re.sub(r'\s+', ' ', clean_title).strip()
    
    url = f'https://api.crossref.org/works?query.title={urllib.parse.quote(clean_title)}&rows=1&select=DOI,title'
    
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Academic; mailto:byyang@connect.hku.hk)'
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        
        items = data.get('message', {}).get('items', [])
        if items:
            return items[0].get('DOI', None)
        return None
    except Exception as e:
        print(f"  Error searching CrossRef: {e}", file=sys.stderr)
        return None


def update_bib_entry(content, key, doi=None, pmid=None, google_scholar_id=None):
    """Add doi, pmid, google_scholar_id fields to a bib entry."""
    # Find the entry
    pattern = re.compile(r'(@article\{' + re.escape(key) + r',\s*\n)(.*?)(\n\})', re.DOTALL)
    match = pattern.search(content)
    if not match:
        return content
    
    body = match.group(2)
    additions = []
    
    # Add DOI if not present and we found one
    if doi and 'doi' not in body.lower().split('=')[0] if '=' in body else True:
        if not re.search(r'^\s*doi\s*=', body, re.MULTILINE):
            additions.append(f'  doi           = {{{doi}}}')
        elif 'XXXXX' in body:
            # Replace placeholder DOI
            content = content.replace('10.1038/s41467-025-XXXXX', doi)
    
    if pmid:
        if not re.search(r'^\s*pmid\s*=', body, re.MULTILINE):
            additions.append(f'  pmid          = {{{pmid}}}')
    
    if google_scholar_id:
        if not re.search(r'^\s*google_scholar_id\s*=', body, re.MULTILINE):
            additions.append(f'  google_scholar_id = {{{google_scholar_id}}}')
    
    if additions:
        addition_text = ',\n'.join(additions)
        # Insert before the closing brace, after the last field
        # Find the last comma-terminated line
        new_body = body.rstrip()
        if not new_body.endswith(','):
            new_body += ','
        new_body += '\n' + addition_text
        content = content[:match.start(2)] + new_body + content[match.end(2):]
    
    return content


def main():
    with open(BIB_FILE, 'r') as f:
        content = f.read()
    
    entries = parse_bib_entries(content)
    print(f"Found {len(entries)} entries in papers.bib")
    
    results = {}
    
    for i, entry in enumerate(entries):
        key = entry['key']
        title = entry['title']
        print(f"\n[{i+1}/{len(entries)}] {key}")
        print(f"  Title: {title[:80]}...")
        
        # Search PubMed
        pmid, doi = search_pubmed(title, entry['first_author'], entry['year'])
        
        if pmid:
            print(f"  PMID: {pmid}")
        if doi:
            print(f"  DOI (PubMed): {doi}")
        
        # If no DOI from PubMed, try CrossRef
        if not doi and entry['doi'] and 'XXXXX' not in entry['doi']:
            doi = entry['doi']
            print(f"  DOI (existing): {doi}")
        elif not doi:
            time.sleep(0.3)
            doi_cr = search_crossref(title)
            if doi_cr:
                doi = doi_cr
                print(f"  DOI (CrossRef): {doi}")
        
        results[key] = {'pmid': pmid, 'doi': doi}
        
        # Rate limiting for PubMed (max 3 requests/second without API key)
        time.sleep(0.5)
    
    # Now update the bib file
    print("\n\nUpdating papers.bib...")
    for key, data in results.items():
        content = update_bib_entry(content, key, doi=data.get('doi'), pmid=data.get('pmid'))
    
    with open(BIB_FILE, 'w') as f:
        f.write(content)
    
    # Summary
    found_doi = sum(1 for v in results.values() if v.get('doi'))
    found_pmid = sum(1 for v in results.values() if v.get('pmid'))
    print(f"\nDone! Found DOI for {found_doi}/{len(entries)} papers, PMID for {found_pmid}/{len(entries)} papers.")
    print("Google Scholar IDs need to be added separately.")


if __name__ == '__main__':
    main()
