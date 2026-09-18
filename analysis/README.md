# Analysis

This directory contains the reproducible computational workflow used for the study's descriptive statistics, association testing, multivariable logistic regression, model validation, security capability scoring, and financial sensitivity analysis.

## Primary Analysis

[`HHS_HIPAA_Breach_Analysis.qmd`](./HHS_HIPPA_Breach_Analysis.qmd)

The Quarto document keeps the Python code, analytical outputs, figures, and concise interpretation in one executable research file.

## Data Dependency

The analysis reads the repository dataset from:

`../data/hhs_hipaa_breach_modeling_data_2009_2026.csv`

## Python Environment

Install the Python dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

Quarto must also be installed separately to render the document.

## Render

From the repository root, render the analysis with:

```bash
quarto render analysis/healthcare_breach_analysis.qmd
```

The workflow uses repository-relative paths so it can be reproduced without local machine-specific file locations.
