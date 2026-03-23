---
layout: page
title: Ct Distribution and Real-Time Transmission Estimation
description: Using population-level viral load distributions to estimate SARS-CoV-2 transmission dynamics in real time
img: assets/img/proj_ct.jpg
importance: 2
category: research
---

Using population-level RT-qPCR cycle threshold (Ct) value distributions to estimate real-time transmission dynamics. We develop and generalise frameworks that incorporate viral load data to track SARS-CoV-2 transmission amid evolving variants and pre-existing immunity, accounting for surveillance heterogeneity and pathogen variability.

<div class="row justify-content-center mt-4 mb-4">
    <div class="col-sm-10">
        {% include figure.liquid path="assets/img/proj_ct.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<h3>Relevant Publications</h3>

<div class="publications">
{% bibliography --query @*[group=ct-distribution] %}
</div>
