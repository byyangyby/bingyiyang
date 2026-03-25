---
layout: page
title: Antibody Responses & Antigenic Evolution
description: Influenza antibody dynamics, cross-reactivity, immune imprinting, and COVID-19 vaccine-induced immunity
img: assets/img/proj_antibody.jpg
importance: 1
category: research
---

How do early-life infections imprint lifelong antibody profiles, and how does this shape cross-reactivity and susceptibility across influenza subtypes? We use longitudinal serological cohorts, Bayesian inference, and deep learning to map the co-evolution of host immunity and viral antigenicity. Tools: SeroMetrics (R package), transformer-based HAI titer prediction.

<div class="row justify-content-center mt-4 mb-4">
    <div class="col-sm-10">
        {% include figure.liquid path="assets/img/proj_antibody.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<h3>Relevant Publications</h3>

<div class="publications">
{% bibliography --query @*[group=antibody-antigenic] %}
</div>
