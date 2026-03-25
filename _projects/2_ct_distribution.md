---
layout: page
title: Ct Distribution and Real-Time Transmission Estimation
description: Using population-level viral load distributions to estimate SARS-CoV-2 transmission dynamics in real time
img: assets/img/proj_ct.jpg
importance: 2
category: research
---

Can population-level viral load distributions replace traditional case counts for real-time epidemic monitoring? We developed methods to estimate effective reproduction numbers (Rt) from PCR cycle threshold (Ct) distributions, enabling surveillance that is robust to changes in testing policy and behavior. These methods have been adopted for influenza surveillance applications.

<div class="row justify-content-center mt-4 mb-4">
    <div class="col-sm-10">
        {% include figure.liquid path="assets/img/proj_ct.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<h3>Relevant Publications</h3>

<div class="publications">
{% bibliography --query @*[group=ct-distribution] %}
</div>
