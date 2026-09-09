# Healthcare Security Architecture Investments

**Using Public Breach Evidence, NIST Guidance, and Financial Decision Analysis**

This applied business analytics project examines how healthcare organizations can use public breach evidence to make more defensible security investment decisions. It connects descriptive analysis, interpretable statistical modeling, model validation, NIST-aligned security capability evaluation, and financial sensitivity analysis.

## Decision flow

```mermaid
flowchart LR
    A[HHS OCR breach data] --> B[Descriptive analysis]
    B --> C[Logistic regression]
    C --> D[Holdout validation & cross-validation]
    D --> E[Security capability evaluation]
    E --> F[Financial scenario & sensitivity analysis]
    F --> G[Phased investment roadmap]
```

The analyses answer different questions. Statistical associations are not treated as causal effects or direct investment recommendations, and the financial model is evaluated separately from the regression.

## Key findings

- **7,877** model-ready reported healthcare breaches; **801 (10.2%)** met the study definition of severe (at least 100,000 individuals affected).
- Network-server involvement was associated with **3.49× adjusted odds** of a severe breach (95% CI: 2.84–4.30).
- Business Associate entity type was associated with **3.55× adjusted odds** relative to Healthcare Providers (95% CI: 2.70–4.66).
- Held-out **ROC-AUC = .776**; five-fold cross-validation mean **ROC-AUC = .757 (SD = .012)**.
- **Monitoring and Detection** ranked first under both equal-weight and risk-focused decision approaches.
- None of the primary financial scenarios produced positive five-year NPV. Sensitivity analysis showed that a **$100,000 initial investment with no annual operating cost required an 11.7% risk reduction to break even**.

## Interpretation

The regression is best understood as an interpretable risk-stratification model for patterns among reported breaches, not as an organization-specific breach predictor. Security rankings provide comparative decision support rather than proof of control effectiveness. Financial feasibility depends on implementation cost, organizational exposure, potential loss, and realistically achievable risk reduction.

## Repository structure

- `analysis/` — computational analysis and documentation
- `data/` — data-source and preparation documentation
- `docs/` — methodology, findings, and decision approach
- `figures/` — exported analytical figures
- `references/` — primary data, standards, and methodological references

## Study scope

The empirical source is the U.S. Department of Health and Human Services Office for Civil Rights breach reporting data. The analysis focuses on reported breaches and therefore does not estimate the annual probability that a particular healthcare organization will experience a breach. The severe-breach threshold of 100,000 affected individuals is a study-defined analytical outcome.

## Core question

> What should be prioritized, why does it deserve priority, and under what financial conditions does the investment make sense?
