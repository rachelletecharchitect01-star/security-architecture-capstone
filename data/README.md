# Data

## Source

The empirical component of this project uses healthcare breach records reported through the **U.S. Department of Health and Human Services Office for Civil Rights (HHS OCR)** breach portal.

Official source: [HHS OCR Breach Portal](https://ocrportal.hhs.gov/ocr/breach/breach_report_hip.jsf)

## Modeling Dataset

The prepared modeling dataset is available at:

[`hhs_hipaa_breach_modeling_data_2009_2026.csv`](./hhs_hipaa_breach_modeling_data_2009_2026.csv)

This analysis-ready dataset is used for descriptive analysis, categorical association testing, and multivariable logistic regression.

## Analytical Sample

| Measure | Value |
|---|---:|
| Source records | 7,884 |
| Model-ready observations | 7,877 |
| Excluded records | 7 |
| Severe breaches | 801 |
| Severe-breach rate | 10.2% |
| Severe-breach threshold | ≥100,000 individuals affected |
| Median individuals affected | 4,000 |
| Mean individuals affected | ~136,399 |

## Variables Used

The analysis uses variables describing breach type, information location, covered-entity type, business-associate involvement, number of individuals affected, and the derived severe-breach outcome.

The binary outcome is coded as severe when a reported breach affects at least **100,000 individuals**.

## Data Preparation

Preparation included record qualification, categorical standardization, creation of modeling indicators, construction of the severe-breach outcome, and validation of the final analytical sample. Seven source records were excluded, leaving **7,877 model-ready observations**.

## Data Scope and Limitations

The data represent **reported breach events**, not a panel of healthcare organizations observed over time. The dataset therefore does not provide an organization-year denominator and cannot be used to estimate the annual probability that a specific healthcare organization will experience a breach.

The severe-breach threshold is a study-defined measure of breach magnitude. It reflects the number of individuals affected and does not capture every operational, clinical, recovery, or financial consequence of an incident.

## APA Source Citation

U.S. Department of Health and Human Services, Office for Civil Rights. (n.d.). *Breach portal: Notice to the Secretary of HHS breach of unsecured protected health information*. https://ocrportal.hhs.gov/ocr/breach/breach_report_hip.jsf
