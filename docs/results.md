# Results

## Breach Profile

The final analytical sample includes **7,877 reported healthcare breaches**, with **801 (10.2%)** classified as severe. The median breach affected approximately **4,000 individuals**, while the mean was approximately **136,399**.

Hacking/IT was present in approximately **60.0%** of breaches, network-server involvement in **45.6%**, and business-associate involvement in approximately **30.0%**.

Network-server incidents had a severe-breach rate of approximately **18.1%** and the strongest categorical association with severity among the evaluated characteristics (**Cramér's V = .239**).

## Logistic Regression

The logistic regression model was statistically significant overall, with likelihood-ratio **p < .001** and **McFadden pseudo-R² = .134**.

Selected adjusted associations included:

| Predictor | Adjusted OR | 95% CI |
|---|---:|---:|
| Network server | **3.49** | 2.84–4.30 |
| Business Associate entity type | **3.55** | 2.70–4.66 |
| Unauthorized access/disclosure | **0.31** | 0.22–0.44 |
| Theft | **0.56** | 0.34–0.93 |
| Paper/film | **0.24** | 0.12–0.50 |

These estimates are interpreted as observational associations rather than causal effects.

## Validation

Held-out ROC-AUC was **0.776**, PR-AUC was **0.249**, and the Brier score was **0.082**. At the training-derived threshold of approximately .111, held-out sensitivity was **0.775** and specificity was **0.638**.

Five-fold stratified cross-validation produced a mean ROC-AUC of **0.757 (SD = 0.012)**, with a range of approximately **0.743–0.773**. All folds converged.

The results indicate moderate and reasonably stable discrimination.
