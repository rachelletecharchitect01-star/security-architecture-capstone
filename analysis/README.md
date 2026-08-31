# Analysis

`run_analysis.py` contains the starter financial decision model and validation rules.

## Planned workflow

1. Load qualified inputs from processed data and the assumption register.
2. Validate units, ranges, missingness, and time alignment.
3. Calculate baseline and residual expected loss.
4. Calculate discounted benefits, costs, ROI, NPV, and payback.
5. Run scenario, sensitivity, and break-even analyses.
6. Save tables and figures to `analysis/outputs/`.
7. Record the code version and input-data version used for reported results.

The starter script exits intentionally until qualified inputs are supplied. This prevents illustrative numbers from being presented as findings.
