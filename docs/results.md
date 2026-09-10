# Results

This section reports the observed results corresponding to the metrics and formulas defined in the Methods. Statistical results are interpreted as associations among reported breaches rather than causal effects.

## Analytical Sample and Severe-Breach Rate

The HHS OCR source contained **7,884 records**. After data qualification, **7,877 observations** were retained for analysis and **7 records** were excluded. A severe breach was defined as one affecting at least 100,000 individuals.

The severe-breach rate was calculated as:

$$
\text{Severe Rate}=\frac{801}{7{,}877}=0.1017\approx10.2\%
$$

Therefore, **801 breaches (10.2%)** were classified as severe and **7,076 (89.8%)** were classified as non-severe.

Breach size was strongly right-skewed. The **median was 4,000 individuals affected**, compared with a **mean of approximately 136,399**, indicating that a smaller number of very large breaches substantially increased the mean.

## Descriptive Results

Hacking/IT was present in **59.97%** of reported breaches, network-server involvement in **45.61%**, and business-associate involvement in **29.99%**.

Selected severe-breach rates were:

| Characteristic | Severe-breach rate |
|---|---:|
| Network server | **18.06%** |
| Hacking/IT | **15.16%** |
| Business-associate involvement | **12.83%** |
| Paper | **0.99%** |

The annual severe-breach rate reached **20.27% in 2023**, followed by **16.73% in 2024** and **12.03% in 2025**. The 2026 value of **8.16%** is based on incomplete-year data and should not be interpreted as a complete annual estimate.

## Categorical Association Results

Pearson chi-square tests evaluated whether breach characteristics were associated with severe-breach status, while Cramér's V summarized the strength of those relationships.

Network-server involvement produced the strongest evaluated categorical association:

$$
\chi^2=450.68,\qquad V=0.239
$$

Hacking/IT produced:

$$
\chi^2=321.42,\qquad V=0.202
$$

Other notable effect sizes included unauthorized access/disclosure (**V = .135**) and paper involvement (**V = .116**). These results indicate association strength; they do not establish that a breach characteristic caused a severe outcome.

## Logistic Regression Results

The multivariable logistic regression model was statistically significant overall:

$$
LR\;\chi^2=692.98,\qquad p<.001
$$

with:

$$
\text{McFadden pseudo-}R^2=0.134
$$

The model converged successfully, and the maximum variance inflation factor was **2.72**, providing no indication of severe multicollinearity among the modeled predictors.

### Fitted Logistic Regression Equation

The fitted model coefficients from the analysis were:

$$
\begin{aligned}
\log\left(\frac{\hat p}{1-\hat p}\right)=\;&-2.6708
+0.7018(\text{Improper Disposal})
-0.4992(\text{Loss})\\
&-0.1341(\text{Other/Multiple})
-0.5793(\text{Theft})
-1.1638(\text{Unauthorized})\\
&+1.2659(\text{Business Associate Entity})
+0.0356(\text{Health Plan})\\
&+0.7329(\text{Clearing House})
-0.5353(\text{Desktop})
-0.5201(\text{EMR})\\
&-0.4727(\text{Laptop})
+1.2507(\text{Network Server})
-1.4246(\text{Paper})\\
&-0.5621(\text{Portable Device})
-0.6721(\text{Business Associate Present})
\end{aligned}
$$

where $\hat p$ is the fitted probability that a reported breach affected at least 100,000 individuals. Indicator variables equal 1 when the corresponding characteristic is present and 0 otherwise. **Hacking/IT** is the breach-type reference category and **Healthcare Provider** is the covered-entity reference category.

The fitted intercept was **−2.6708**. The coefficient for network-server involvement was **1.2507**, corresponding to an adjusted odds ratio of $e^{1.2507}=3.49$. The coefficient for Business Associate entity type was **1.2659**, corresponding to an adjusted odds ratio of approximately **3.55**. Negative coefficients indicate lower adjusted log-odds relative to the applicable reference category or absence of the indicator, holding the other modeled variables constant.

### Adjusted Odds Ratios

| Predictor | Adjusted OR | 95% CI | p-value | Interpretation |
|---|---:|---:|---:|---|
| Network server | **3.49** | 2.84–4.30 | <.001 | Higher adjusted odds |
| Business Associate entity type | **3.55** | 2.70–4.66 | <.001 | Higher adjusted odds |
| Unauthorized access/disclosure | **0.31** | 0.22–0.44 | <.001 | Lower adjusted odds |
| Theft | **0.56** | 0.34–0.93 | .023 | Lower adjusted odds |
| Paper | **0.24** | 0.12–0.50 | <.001 | Lower adjusted odds |

Covered Entity Type = Business Associate and Business Associate Present represent different predictors and should not be interpreted as interchangeable measures.

## Holdout Validation Results

The stratified split produced **6,301 training observations** and **1,576 held-out test observations**. Severe-breach prevalence remained approximately 10.2% in both samples.

The training-derived Youden threshold was:

$$
\text{Threshold}=0.1106\approx0.111
$$

The threshold was applied unchanged to the held-out test sample. The resulting confusion matrix was:

| | Predicted Non-Severe | Predicted Severe |
|---|---:|---:|
| **Observed Non-Severe** | TN = **903** | FP = **513** |
| **Observed Severe** | FN = **36** | TP = **124** |

### Sensitivity

$$
\text{Sensitivity}=\frac{124}{124+36}=0.775
$$

The model therefore identified **77.5% of severe breaches** in the held-out sample.

### Specificity

$$
\text{Specificity}=\frac{903}{903+513}=0.638
$$

The model correctly classified **63.8% of non-severe breaches**.

### Precision

$$
\text{Precision}=\frac{124}{124+513}=0.195
$$

Approximately **19.5% of breaches classified as severe were actually severe**. This lower precision should be interpreted in the context of the approximately 10% prevalence of severe breaches and the threshold selected to balance sensitivity and specificity.

### F1 Score

$$
F_1=2\left(\frac{0.195\times0.775}{0.195+0.775}\right)\approx0.311
$$

### Probability and Discrimination Metrics

Held-out model performance was:

| Metric | Result |
|---|---:|
| ROC-AUC | **0.776** |
| PR-AUC | **0.249** |
| Brier score | **0.082** |
| Sensitivity | **0.775** |
| Specificity | **0.638** |
| Precision | **0.195** |
| F1 | **0.311** |

The held-out ROC-AUC of **.776** indicates moderate discrimination. The Brier score of **.082** summarizes the accuracy of the predicted probabilities, with lower values indicating smaller squared probability errors.

## Cross-Validation Results

Five-fold stratified cross-validation was performed within the training sample. ROC-AUC values were:

| Fold | ROC-AUC |
|---|---:|
| 1 | .7525 |
| 2 | .7653 |
| 3 | .7426 |
| 4 | .7730 |
| 5 | .7492 |

The mean and standard deviation were:

$$
\overline{AUC}=0.7565\approx0.757
$$

$$
SD_{AUC}=0.0124\approx0.012
$$

The range was **.743–.773**, and all five folds converged. The relatively small variation across folds supports stable discrimination across the resampled training subsets. This is an internal stability assessment rather than external validation.

## Security Capability Evaluation

The statistical results were combined with supporting evidence, NIST alignment, cost, feasibility, operational impact, dependencies, and time to value in the security capability evaluation. The weighted score defined in the Methods was calculated under both equal-weight and risk-focused assumptions.

| Capability | Equal-weight score | Equal-weight rank | Risk-focused score | Risk-focused rank |
|---|---:|---:|---:|---:|
| Monitoring and Detection | **4.50** | **1** | **4.65** | **1** |
| Third-Party Access and Risk Governance | 4.12 | 2 | 4.15 | 4 |
| Network and Workload Security | 4.00 | 3 (tie) | **4.30** | **2** |
| IAM / Zero-Trust Access | 4.00 | 3 (tie) | **4.20** | **3** |
| Incident Response and Recovery | 3.12 | 5 | 3.15 | 5 |

**Monitoring and Detection ranked first under both weighting approaches.** Network and Workload Security moved upward under risk-focused weighting. The comparison shows which priorities were relatively stable and which were more sensitive to weighting assumptions.

## Financial Decision Results

The financial analysis used the formulas defined in the Methods to evaluate annualized loss expectancy (ALE), avoided loss, annual net benefit, five-year NPV, payback, and break-even risk reduction under alternative scenarios.

### Primary Scenario Calculations

| Scenario | ALE | Avoided loss | Annual net benefit | 5-year NPV | Break-even risk reduction |
|---|---:|---:|---:|---:|---:|
| Low | $105,634 | $10,563 | −$89,437 | **−$680,258** | **143.9%** |
| Expected | $177,314 | $44,329 | −$155,671 | **−$1,248,899** | **171.4%** |
| High | $248,994 | $99,598 | −$300,402 | **−$2,445,165** | **244.1%** |

In the expected scenario:

$$
ALE=0.235\times0.1016885\times\$7.42M\approx\$177{,}314
$$

With an assumed 25% risk reduction:

$$
\text{Avoided Loss}=\$177{,}314\times0.25\approx\$44{,}329
$$

After the $200,000 annual operating cost:

$$
\text{Annual Net Benefit}=\$44{,}329-\$200{,}000=-\$155{,}671
$$

The resulting five-year NPV was approximately **−$1.25 million**. Because annual net benefit was negative in all three primary scenarios, none produced a finite payback period.

Break-even risk reductions above 100% in all primary scenarios indicate that the modeled investments could not reach break-even through proportional risk reduction alone under those cost and exposure assumptions.

## Break-Even and Sensitivity Results

Cost sensitivity materially changed the amount of risk reduction required to break even:

| Initial cost | Annual operating cost | Required risk reduction |
|---:|---:|---:|
| $100,000 | $0 | **11.7%** |
| $250,000 | $50,000 | **57.5%** |
| $500,000 | $100,000 | **115.0%** |

For the lowest-cost tested case, the break-even calculation indicates that an investment would need to reduce modeled expected loss by approximately **11.7%** for the present value of benefits to equal the investment cost.

Risk sensitivity was also evaluated while holding the initial investment at $250,000, annual operating cost at $50,000, assumed risk reduction at 30%, discount rate at 1.3%, and horizon at five years. The most favorable tested exposure/loss combination produced an NPV of approximately **−$6,231**, approaching but not crossing break-even.

These results show that financial feasibility is highly dependent on implementation cost, organizational exposure, potential loss, and realistically achievable risk reduction. The negative primary NPVs are therefore interpreted as scenario results rather than evidence that security investment has no value.

## Combined Results

The analysis supports a phased investment sequence beginning with **Monitoring and Detection**, followed by **Network and Workload Security**, **IAM / Zero-Trust Access**, and **Third-Party Access and Risk Governance**, with **Incident Response and Recovery** treated as a cross-cutting capability.

The statistical and security analyses identify where greater attention may be warranted, while the financial analysis addresses a different question: **under what cost, exposure, loss, and risk-reduction conditions does an investment become economically supportable?** Together, these results connect the empirical breach analysis to a transparent security investment decision process without treating observational associations as causal evidence.