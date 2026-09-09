# Methodology

## Research design

The project uses an applied observational design to examine characteristics associated with severe reported healthcare breaches and connect those findings to security and financial decision analysis.

## Statistical analysis

A severe breach is defined as a reported breach affecting at least 100,000 individuals. Descriptive statistics and categorical association measures are followed by multivariable logistic regression.

Predictors include breach type, information-location indicators, covered-entity type, and business-associate involvement. Hacking/IT Incident and Healthcare Provider serve as reference categories. Results are interpreted using adjusted odds ratios, 95% confidence intervals, likelihood-ratio testing, and McFadden pseudo-R². Multicollinearity is assessed with variance inflation factors.

## Validation

Predictive discrimination is evaluated with a stratified 80/20 training-test split. The classification threshold is selected from the training data using Youden's J statistic and applied unchanged to the held-out test data. Five-fold stratified cross-validation is conducted within the training sample to assess ROC-AUC stability while preserving the held-out sample for final evaluation.

The model is interpreted as an explainable risk-stratification model, not an organization-specific breach predictor.

## Security decision analysis

Empirical findings are treated as one source of evidence rather than direct prescriptions. Candidate capabilities are evaluated using empirical risk relevance, evidence strength, NIST alignment, cost, feasibility, operational impact, dependencies, and time to value. Equal-weight and risk-focused approaches are compared to assess ranking sensitivity.

## Financial analysis

Financial scenarios evaluate annualized loss expectancy, avoided loss, implementation and operating costs, five-year NPV, payback, and break-even risk reduction. Sensitivity analysis tests how financial feasibility changes as costs, exposure, potential loss, and assumed risk reduction change.
