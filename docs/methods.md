# Methods

## Research Design

The study uses a retrospective observational design combined with decision analysis. Public HHS OCR breach records are used to examine characteristics associated with severe reported healthcare breaches. The statistical evidence is then considered alongside NIST guidance and financial assumptions to support security investment decisions.

A **severe breach** is defined as a reported breach affecting at least 100,000 individuals:

$$
Y_i = \begin{cases}
1, & \text{if Individuals Affected}_i \ge 100{,}000 \\
0, & \text{otherwise}
\end{cases}
$$

The analysis evaluates severity among reported breaches; it does not estimate the probability that a particular healthcare organization will experience a breach.

## Data Preparation

The HHS OCR source contained 7,884 records. After qualification and preparation, 7,877 observations were included in the analytical sample. Records were screened for missing values, duplicate identifiers, and potential duplicate observations while preserving the source data.

## Descriptive and Association Analysis

Descriptive statistics summarize breach size, breach type, information location, covered-entity characteristics, business-associate involvement, and annual patterns. Because breach size is strongly right-skewed, medians, percentiles, counts, and proportions are emphasized rather than relying on means alone.

Categorical relationships with severe-breach status are evaluated using Pearson's chi-square statistic:

$$
\chi^2 = \sum \frac{(O-E)^2}{E}
$$

where $O$ is the observed count and $E$ is the expected count.

Association strength is summarized with **Cramér's V**:

$$
V = \sqrt{\frac{\chi^2}{n\,\min(r-1,c-1)}}
$$

where $n$ is the sample size and $r$ and $c$ are the numbers of rows and columns in the contingency table.

## Logistic Regression

Multivariable logistic regression estimates adjusted associations between observable breach characteristics and the probability that a reported breach is severe. Predictors include breach type, information-location indicators, covered-entity type, and business-associate involvement. Hacking/IT Incident and Healthcare Provider serve as reference categories.

The model is expressed as:

$$
\log\left(\frac{p_i}{1-p_i}\right)=\beta_0+\beta_1X_{1i}+\beta_2X_{2i}+\cdots+\beta_kX_{ki}
$$

where $p_i=P(Y_i=1\mid X_i)$ is the modeled probability of a severe breach.

Adjusted odds ratios are calculated as:

$$
OR_j=e^{\beta_j}
$$

Odds ratios are reported with 95% confidence intervals and p-values. Overall model fit is evaluated using likelihood-ratio testing and McFadden pseudo-$R^2$.

Multicollinearity is assessed using the variance inflation factor:

$$
VIF_j=\frac{1}{1-R_j^2}
$$

where $R_j^2$ is obtained by regressing predictor $j$ on the remaining predictors.

## Model Validation and Performance Metrics

A stratified 80/20 training-test split is used for validation. The classification threshold is selected from the training data using **Youden's J statistic** and then applied unchanged to the held-out test sample:

$$
J=\text{Sensitivity}+\text{Specificity}-1
$$

Five-fold stratified cross-validation is conducted within the training sample to assess ROC-AUC stability while preserving the held-out test set for final evaluation.

Classification outcomes are summarized using true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN).

**Sensitivity / Recall**

$$
\text{Sensitivity}=\frac{TP}{TP+FN}
$$

**Specificity**

$$
\text{Specificity}=\frac{TN}{TN+FP}
$$

**Precision**

$$
\text{Precision}=\frac{TP}{TP+FP}
$$

**F1 Score**

$$
F_1=2\left(\frac{\text{Precision}\times\text{Sensitivity}}{\text{Precision}+\text{Sensitivity}}\right)
$$

**ROC-AUC** evaluates the model's ability to discriminate between severe and non-severe breaches across classification thresholds. **PR-AUC** summarizes the precision-recall relationship and is included because severe breaches are the less common outcome class.

Probability accuracy is evaluated using the **Brier score**:

$$
BS=\frac{1}{n}\sum_{i=1}^{n}(p_i-y_i)^2
$$

where $p_i$ is the predicted probability and $y_i$ is the observed binary outcome. Lower Brier scores indicate more accurate probability estimates. Calibration is evaluated by comparing predicted probabilities with observed severe-breach frequencies.

The model is interpreted as an explainable risk-stratification model rather than an organization-specific breach predictor.

## Security Capability Evaluation

Empirical findings are treated as one source of evidence rather than direct technology recommendations. Candidate capabilities are evaluated on a 1–5 scale using empirical relevance, supporting evidence, NIST alignment, implementation cost, feasibility, operational impact, dependencies, and time to value.

For capability $i$, a weighted decision score is represented as:

$$
S_i=\sum_{j=1}^{m}w_jx_{ij}
$$

where $x_{ij}$ is the score for capability $i$ on criterion $j$, $w_j$ is the criterion weight, and the weights sum to 1. Equal-weight and risk-focused scoring approaches are compared to evaluate whether rankings are sensitive to weighting assumptions.

## Financial Decision Analysis

Financial analysis evaluates the conditions under which candidate security investments may be economically supportable. Inputs that are not observed in the HHS breach data are treated explicitly as scenario assumptions.

### Annualized Loss Expectancy

Baseline annualized loss expectancy is modeled as:

$$
ALE=f\times p_s\times L
$$

where $f$ is assumed annual breach frequency, $p_s$ is the probability that a reported breach is severe, and $L$ is the estimated financial loss associated with a severe breach.

### Avoided Loss and Annual Net Benefit

If $r$ represents the assumed proportional risk reduction from an investment:

$$
\text{Avoided Loss}=ALE\times r
$$

Annual net benefit is:

$$
B=\text{Avoided Loss}-C_{op}
$$

where $C_{op}$ is annual operating cost.

### Net Present Value

Five-year net present value is calculated as:

$$
NPV=-C_0+\sum_{t=1}^{T}\frac{B_t}{(1+d)^t}
$$

where $C_0$ is the initial investment, $B_t$ is annual net benefit in year $t$, $d$ is the discount rate, and $T$ is the investment horizon. A positive NPV indicates that modeled benefits exceed modeled costs under the stated assumptions.

### Break-Even Risk Reduction

Break-even analysis solves for the minimum proportional risk reduction $r^*$ that produces an NPV of zero:

$$
0=-C_0+\sum_{t=1}^{T}\frac{ALE\times r^*-C_{op}}{(1+d)^t}
$$

When ALE and annual operating costs are constant across years, this can be written as:

$$
r^*=\frac{C_0+C_{op}\displaystyle\sum_{t=1}^{T}(1+d)^{-t}}{ALE\displaystyle\sum_{t=1}^{T}(1+d)^{-t}}
$$

A required reduction above 1.0 (100%) indicates that break-even cannot be achieved through proportional risk reduction alone under the modeled assumptions.

### Payback Period

For scenarios with positive annual net benefit, simple payback is:

$$
\text{Payback Period}=\frac{C_0}{B}
$$

No finite payback period is reported when annual net benefit is zero or negative.

## Sensitivity Analysis

Sensitivity analysis varies initial investment cost, annual operating cost, annual breach frequency, financial loss per severe breach, and assumed risk reduction. The purpose is to evaluate how changes in cost, exposure, loss, and effectiveness assumptions affect NPV and break-even conditions rather than treating any single scenario as a universal estimate of security investment value.
