---
layout: page
permalink: /repositories/
title: repositories
description: Code and data repositories for published research.
nav: true
nav_order: 4
---

## Software & Product

- **SeroMetrics** — R package for serological analysis: [GitHub](https://github.com/byyangyby/SeroMetrics)
- **Influenza HAI Prediction** — Deep learning-based HAI titer prediction: [Hugging Face](https://huggingface.co/spaces/yyf031/Influenza_A_HAI_Titer_Prediction)

---

## Code Repositories

| Year | Repository | Journal |
|------|-----------|---------|
| 2025 | [influenza_A_cross-reactivity](https://github.com/byyangyby/influenza_A_cross-reactivity) | *Nature Microbiology* |
| 2025 | [Zenodo: nAb duration & correlates of protection](https://doi.org/10.5281/zenodo.15227371) | *Nature Communications* |
| 2024 | [importation_risk](https://github.com/byyangyby/importation_risk) | *Lancet Regional Health – Western Pacific* |
| 2022 | [fractional_dose_review](https://github.com/byyangyby/fractional_dose_review) | *BMC Medicine* |
| 2022 | [ct_rt_hk](https://github.com/byyangyby/ct_rt_hk) | *Nature Communications* |
| 2022 | [Fluscape_Periodicity](https://github.com/UF-IDD/Fluscape_Periodicity) | *eLife* |
| 2021 | [US_County_Rt](https://github.com/UF-IDD/US_County_Rt) | *Nature Communications* |
| 2021 | [Modeling_Aedes_Florida](https://github.com/UF-IDD/Modeling_Aedes_Florida) | *PLoS Neglected Tropical Diseases* |
| 2020 | [Fluscape_Paired_Serology](https://github.com/UF-IDD/Fluscape_Paired_Serology) | *PLoS Pathogens* |

---

{% if site.data.repositories.github_users %}

## GitHub

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.liquid username=user %}
  {% endfor %}
</div>
{% endif %}
