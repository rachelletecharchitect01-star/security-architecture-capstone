# Analysis Protocol

## Purpose

Predefine the analytical decisions needed to translate public evidence into a transparent security-investment decision model.

## Required decisions before analysis

- Security-architecture investment or comparison
- Decision-maker and organizational perspective
- Unit of analysis
- Base year and currency
- Time horizon
- Discount rate
- Baseline risk definition
- Consequence categories
- Control-effectiveness definition
- Cost categories
- Primary decision criterion
- Scenario ranges
- Missing-data rules
- Outlier rules
- Validation tests

## Evidence hierarchy

Classify every input as one of the following:

1. **Observed:** Directly present in a qualified dataset.
2. **Derived:** Calculated from observed values using documented transformations.
3. **Literature-derived:** Taken from a cited study or authoritative report.
4. **Assumed:** Selected for scenario analysis when direct evidence is unavailable.

## Core equations

Let (p) denote annual incident probability, (L) expected consequence, (e) control effectiveness, (C_0) initial cost, (C_t) recurring cost, (r) discount rate, and (T) the time horizon.

- Baseline expected annual loss: (EAL_0 = pL)
- Residual expected annual loss: (EAL_1 = pL(1-e))
- Expected annual avoided loss: (B = EAL_0 - EAL_1)
- Net present value: (NPV = -C_0 + sum_{t=1}^{T}(B_t-C_t)/(1+r)^t)
- ROI: (ROI = (PV(B)-PV(C))/PV(C))

## Minimum sensitivity analysis

- Control effectiveness
- Incident probability
- Expected consequence
- Initial investment cost
- Recurring cost
- Discount rate
- Time horizon

## Validation checks

- Probabilities and effectiveness values remain within [0, 1].
- Monetary values use a consistent currency and base year.
- Source totals reconcile where possible.
- Zero-effectiveness produces zero avoided loss.
- Higher effectiveness does not increase residual loss.
- NPV responds correctly to cost and benefit changes.
- Reported tables can be regenerated from committed code and qualified inputs.
