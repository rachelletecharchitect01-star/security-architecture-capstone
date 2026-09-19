# Key Findings

## 1. Network-Server Breaches Were Strongly Associated with Severity

Network-server involvement had the strongest evaluated categorical association with severe-breach status and was associated with **3.49 times higher adjusted odds** of a severe breach, holding the other modeled characteristics constant. Exploratory clustering independently identified a business-associate hacking and network-server profile with the highest cluster severe-breach rate (**17.77%**).

## 2. Business Associate Entity Type Was an Important Risk Indicator

Business Associate entities had **3.55 times higher adjusted odds** of a severe breach than Healthcare Providers after adjustment for the other modeled characteristics.

## 3. The Model Demonstrated Moderate and Stable Discrimination

Held-out **ROC-AUC was .776**. Five-fold stratified cross-validation produced a mean ROC-AUC of **.757 (SD = .012)**. At the training-derived threshold of **.1106**, holdout sensitivity was **.775** and specificity was **.638**, with 124 of 160 severe breaches identified. These results support use of the model for risk stratification and interpretation rather than organization-specific breach prediction.

## 4. Monitoring and Detection Was the Most Consistent Security Priority

Monitoring and Detection ranked **first under both equal-weight and risk-focused scoring**. Network and Workload Security ranked second when greater weight was placed on risk evidence.

## 5. Financial Feasibility Depended on Cost and Achievable Risk Reduction

None of the primary scenarios produced positive five-year NPV or finite payback. Lower implementation costs materially improved the financial case. In the lowest-cost sensitivity scenario, a **$100,000 initial investment with no annual operating cost required an 11.7% risk reduction to break even**.

## Overall Finding

The evidence supports prioritizing **Monitoring and Detection**, followed by **Network and Workload Security**, while evaluating implementation decisions separately based on **cost, organizational exposure, potential loss, and achievable risk reduction**.

## Supplementary Validation

An independently implemented KNIME logistic-regression benchmark produced holdout **ROC-AUC .753**. At the same risk threshold of **.1106**, it identified **120 of 160 severe breaches** with sensitivity **.750**. A pruned decision tree produced **ROC-AUC .690** and reinforced network-server involvement as an interpretable discriminator. The Python model remains the primary analysis.
