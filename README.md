# Security Architecture Capstone

## Security Architecture Investment and Organizational Risk

This repository is the working home for an MS Business Analytics capstone examining how publicly available evidence can be used to evaluate the business value of security-architecture investments.

The project is designed as a transparent, reproducible secondary-data study. It connects security architecture, cyber-risk indicators, incident consequences, and financial decision analysis without relying on confidential organizational data.

> **Working status:** Framework and starter materials. Research questions, data sources, assumptions, and model specifications remain subject to academic review.

## Working research question

**How can organizations use public data and transparent financial assumptions to estimate the potential risk-reduction value and return on investment of security-architecture investments?**

Supporting questions:

1. Which public indicators can represent cyber-risk exposure, incident likelihood, and incident consequence?
2. How sensitive are ROI conclusions to assumptions about implementation cost, control effectiveness, and avoided loss?
3. Under what conditions does a proposed security-architecture investment produce positive expected value?
4. Which assumptions contribute most to uncertainty in the decision?

## Study at a glance

| Component | Planned approach |
|---|---|
| Study type | Quantitative secondary-data decision analysis |
| Unit of analysis | Defined organizational, industry, or scenario-level observation |
| Evidence base | Public government, regulatory, industry, and research sources |
| Primary outputs | Expected-loss estimates, ROI, net present value, payback period, and sensitivity results |
| Uncertainty | Scenario analysis and Monte Carlo simulation where inputs support it |
| Reproducibility | Versioned data inventory, documented transformations, scripted analysis, and explicit assumptions |
| Intended use | Graduate capstone research and decision-support demonstration |

## Repository structure

- `paper/` — manuscript outline and drafting materials
- `presentation/` — defense-deck outline and speaking-plan starter
- `data/raw/` — immutable source-data landing area
- `data/processed/` — analysis-ready datasets
- `data/templates/` — source inventory and assumption templates
- `analysis/` — reproducible Python analysis scaffold
- `appendices/` — protocols, variable definitions, and model assumptions
- `references/` — literature and citation tracking
- `project_management/` — fast-track schedule and decision log

## Analytical framework

The core decision model compares the expected economic loss before and after a security-architecture investment.

```text
Baseline expected loss = incident probability × expected consequence

Residual expected loss = baseline expected loss × (1 − assumed control effectiveness)

Expected annual benefit = baseline expected loss − residual expected loss

ROI = (discounted benefits − discounted costs) / discounted costs
```

The final model will separate sourced observations from analyst assumptions. It will also report sensitivity ranges so that results are not presented as more certain than the evidence permits.

## Quick start

1. Review `CAPSTONE_3MONTH_FASTTRACK.md`.
2. Refine the research question in `paper/PAPER_OUTLINE.md`.
3. Record candidate sources in `data/templates/source_inventory.csv`.
4. Document every modeling assumption in `data/templates/assumption_register.csv`.
5. Place downloaded source files in `data/raw/` without altering them.
6. Build cleaned datasets in `data/processed/`.
7. Run the analysis scaffold from the repository root:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python analysis/run_analysis.py
```

## Research guardrails

- Use only lawfully accessible public or properly licensed data.
- Preserve raw files and document source URLs, access dates, licenses, and transformations.
- Do not infer causation from observational associations without an appropriate identification strategy.
- Keep empirical inputs, literature-derived parameters, and scenario assumptions distinguishable.
- Avoid publishing sensitive security configurations or operational details.
- Report uncertainty, limitations, and alternative assumptions alongside point estimates.

## Current milestone

The repository contains the project framework and starter files. The next milestone is to finalize the problem statement, select the specific security-architecture investment or comparison, and qualify the public datasets before modeling begins.
