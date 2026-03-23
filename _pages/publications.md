---
layout: page
permalink: /publications/
title: publications
description: Research grouped by theme. Only publications with first, last, or corresponding authorship are listed here. See my <a href="https://scholar.google.com/citations?user=1IQInjgAAAAJ">Google Scholar</a> for a complete list.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

{% include bib_search.liquid %}

<div class="publications">

<h2>Antibody Responses & Antigenic Evolution</h2>

<p>How life course exposures shape antibody profiles and cross-reactive responses across influenza subtypes, and how deep learning can reconstruct antigenic evolution from serological data. We also quantify how COVID-19 vaccine-induced immunity wanes over time, identify correlates of protection, and disentangle the effects of prior infection and antigenic drift on vaccine effectiveness.</p>

{% bibliography --query @*[group=antibody-antigenic] %}

<h2>Ct Distribution and Real-Time Transmission Estimation</h2>

<p>Using population-level RT-qPCR cycle threshold (Ct) value distributions to estimate real-time transmission dynamics. We develop and generalise frameworks that incorporate viral load data to track SARS-CoV-2 transmission amid evolving variants and pre-existing immunity, accounting for surveillance heterogeneity and pathogen variability.</p>

{% bibliography --query @*[group=ct-distribution] %}

<h2>COVID-19 Transmission Dynamics and Intervention Effectiveness</h2>

<p>Understanding how SARS-CoV-2 spreads through populations and how interventions modify transmission. We apply spatiotemporal models and epidemiological surveillance data to evaluate the impact of specific non-pharmaceutical interventions across diverse settings and epidemic waves.</p>

{% bibliography --query @*[group=covid-transmission] %}

<h2>Travel Controls & Importation Risk</h2>

<p>Evaluating the effectiveness of border control measures — travel restrictions, quarantine requirements, and targeted surveillance — in delaying and reducing importation of COVID-19. Our work quantifies the role of travel volume and control intensity in shaping importation risk, informing evidence-based border policy during pandemics.</p>

{% bibliography --query @*[group=travel-control] %}

</div>
