# Methods

## Research Design

The study uses an applied observational design to examine characteristics associated with severe reported healthcare breaches and to connect empirical findings with security and financial decision analysis.

## Data Preparation

The HHS OCR source contained 7,884 records. After qualification and preparation, 7,877 observations were included in the analytical sample. A severe breach was defined as a reported breach affecting at least 100,000 individuals.

## Descriptive and Association Analysis

Descriptive statistics summarize breach size, breach type, information location, covered-entity characteristics, business-associate involvement, and temporal patterns. Chi-square testing and Cramér's V are used to evaluate categorical relationships with severity.

## Logistic Regression

Multivariable logistic regression estimates adjusted associations between breach characteristics and the probability that a reported breach meets the severe-breach definition. Predictors include breach type, information-location indicators, covered-entity type, and business-associate involvement. Hacking/IT Incident and Healthcare Provider serve as reference categories.

Results are reported using adjusted odds ratios, 95% confidence intervals, likelihood-ratio testing, and McFadden pseudo-R². Variance inflation factors are used to assess multicollinearity.

## Model Validation

A stratified 80/20 training-test split is used for validation. The classification threshold is selected from the training data using Youden's J statistic and then applied unchanged to the held-out test sample.

Evaluation includes ROC-AUC, PR-AUC, Brier score, sensitivity, specificity, precision, F1 score, and the confusion matrix. Five-fold stratified cross-validation is performed within the training sample to evaluate ROC-AUC stability while preserving the held-out test set for final evaluation.

## Security Capability Evaluation

Regression findings are treated as one source of evidence rather than direct technology recommendations. Candidate capabilities are evaluated using empirical relevance, supporting evidence, NIST alignment, implementation cost, feasibility, operational impact, dependencies, and time to value.

Equal-weight and risk-focused scoring approaches are compared to assess ranking sensitivity.

## Financial Decision Analysis

The financial analysis evaluates annualized loss expectancy, avoided expected loss, initial investment, recurring operating cost, five-year NPV, payback, break-even risk reduction, and sensitivity to key assumptions.
