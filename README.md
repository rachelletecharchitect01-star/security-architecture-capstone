# Healthcare Security Architecture Investments

**Using Public Breach Evidence, NIST Guidance, and Financial Decision Analysis**

## Overview

Healthcare organizations make security investment decisions under uncertainty. This research examines how public healthcare breach evidence, statistical analysis, security guidance, and financial decision analysis can be connected to support security investment decisions.

## Research Question

> **“How can public healthcare breach evidence be used to identify security priorities and evaluate the financial conditions under which security architecture investments are supportable?”**

### Research Objectives

1. Examine patterns in the frequency and severity of reported healthcare breaches.
2. Identify observable breach characteristics associated with severe outcomes after adjustment for other characteristics.
3. Map empirical findings to relevant security capabilities using NIST guidance.
4. Evaluate candidate security capabilities using defined decision criteria and alternative weighting assumptions.
5. Evaluate the financial conditions under which candidate security investments become supportable using cost, exposure, loss, and risk-reduction assumptions.
6. Develop a phased security investment roadmap informed by the combined statistical, security, and financial analysis.

## Data Source

**U.S. Department of Health and Human Services, Office for Civil Rights (HHS OCR) Breach Portal**

## Research Approach

```mermaid
flowchart LR
    A[HHS OCR Data] --> B[Descriptive Analysis]
    B --> C[Statistical Analysis]
    C --> D[Model Validation]
    D --> E[Security Capability Evaluation]
    E --> F[Financial Decision Analysis]
    F --> G[Investment Roadmap]
```

The research separates statistical evidence from security and financial decision-making. Observed associations are not interpreted as causal effects, and statistical results are not treated as direct recommendations to purchase a particular technology.

## Analytical Methods

The quantitative analysis uses descriptive statistics, categorical association testing, and multivariable logistic regression. Model performance and stability are evaluated using a stratified holdout sample and five-fold stratified cross-validation.

The security decision analysis connects empirical evidence with NIST guidance and evaluates candidate capabilities using multiple decision criteria and alternative weighting approaches. Financial analysis examines annualized loss expectancy, avoided loss, net present value, payback, break-even conditions, and sensitivity to key assumptions.

## Research Structure

| Stage | Purpose |
|---|---|
| Descriptive analysis | Examine breach patterns and severity |
| Statistical modeling | Estimate adjusted associations with severe outcomes |
| Model validation | Evaluate discrimination and stability |
| Security capability evaluation | Translate evidence into comparable security priorities |
| Financial decision analysis | Evaluate financial feasibility and break-even conditions |
| Investment roadmap | Sequence security priorities based on the combined analysis |

## Scope

The research examines reported healthcare breach events and uses an observational design. Statistical relationships are interpreted as associations rather than causal effects. Financial analysis is scenario-based and is intended to evaluate decision conditions rather than establish a universal return on security investment.

## Standards and Guidance

The security decision analysis is informed by **NIST Cybersecurity Framework 2.0**, **NIST SP 800-30**, and **NIST SP 800-207**.
