# Healthcare Security Architecture Investments

**Using Public Breach Evidence, NIST Guidance, and Financial Decision Analysis**

## Overview

Healthcare organizations must decide where to invest limited security resources. This research uses public healthcare breach data to study severe breach patterns and then connects that evidence to security priorities and financial decision-making.

The study moves through three main questions: **What does the breach data show? What security capabilities should receive greater consideration? Under what conditions would those investments make financial sense?**

## Research Question

> **“How can healthcare breach data inform security investment decisions?”**

### Research Objectives

1. **Analyze breach patterns** to understand the frequency and severity of reported healthcare breaches.
2. **Identify factors associated with severe breaches** using statistical analysis and logistic regression.
3. **Connect the statistical evidence to security capabilities** using NIST guidance.
4. **Compare security priorities** using defined decision criteria and alternative weighting approaches.
5. **Evaluate financial feasibility** using cost, breach exposure, potential loss, risk reduction, NPV, payback, and break-even analysis.
6. **Develop a phased investment roadmap** that brings the statistical, security, and financial analyses together.

## Data Source

**U.S. Department of Health and Human Services, Office for Civil Rights (HHS OCR) Breach Portal**

## Research Approach

```mermaid
flowchart LR
    A[Healthcare Breach Data] --> B[Breach Analysis]
    B --> C[Statistical Modeling]
    C --> D[Model Validation]
    D --> E[Security Priorities]
    E --> F[Financial Evaluation]
    F --> G[Investment Roadmap]
```

The statistical analysis identifies patterns and associations in reported breaches. Those findings are then used as evidence in a separate evaluation of security capabilities. The financial analysis evaluates whether candidate investments are economically supportable under different assumptions.

## Methods

The research uses descriptive statistics and categorical association analysis to examine breach patterns. Multivariable logistic regression is used to estimate which observable characteristics are associated with severe reported breaches after accounting for other characteristics in the model. Holdout testing and five-fold cross-validation are used to evaluate model performance and stability.

Security capabilities are then evaluated using the statistical evidence, NIST guidance, and defined decision criteria. Alternative weighting approaches are used to examine whether priorities change when greater emphasis is placed on risk-related criteria.

The financial analysis evaluates investment costs and expected avoided losses using annualized loss expectancy, net present value, payback, break-even analysis, and sensitivity analysis.

## Scope

The study examines associations in reported healthcare breach data rather than causal effects. The statistical model is used to support interpretation and risk stratification, not to predict whether a specific healthcare organization will experience a severe breach. Financial analysis is scenario-based and evaluates the conditions under which an investment may be financially supportable.

## Standards and Guidance

The security analysis is informed by **NIST Cybersecurity Framework 2.0**, **NIST SP 800-30**, and **NIST SP 800-207**.
