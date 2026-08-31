# Variable Dictionary Starter

| Variable | Definition | Type | Unit | Source class | Allowed range | Notes |
|---|---|---|---|---|---|---|
| annual_incident_probability | Probability of an in-scope incident during one year | Model input | Proportion | Observed, derived, or literature-derived | 0–1 | Define incident scope precisely |
| expected_consequence | Expected economic consequence conditional on an incident | Model input | Currency | Observed, derived, or literature-derived | ≥ 0 | State included cost categories |
| control_effectiveness | Proportional reduction in modeled expected loss | Model input | Proportion | Literature-derived or assumed | 0–1 | Subject to sensitivity analysis |
| initial_cost | Up-front implementation cost | Model input | Currency | Observed or assumed | > 0 | Base-year currency |
| annual_operating_cost | Recurring annual cost | Model input | Currency/year | Observed or assumed | ≥ 0 | Include labor and maintenance if in scope |
| time_horizon_years | Evaluation period | Model input | Years | Assumed | Integer ≥ 1 | Align to decision context |
| discount_rate | Annual rate used to discount future cash flows | Model input | Proportion | Literature-derived or assumed | 0–1 | Justify chosen rate |
| baseline_expected_annual_loss | Expected loss before investment | Derived outcome | Currency/year | Derived | ≥ 0 | (p × L) |
| residual_expected_annual_loss | Expected loss after investment | Derived outcome | Currency/year | Derived | ≥ 0 | Baseline loss × ((1-e)) |
| expected_annual_avoided_loss | Modeled annual benefit | Derived outcome | Currency/year | Derived | ≥ 0 | Baseline minus residual loss |
| net_present_value | Discounted benefits minus discounted costs | Decision outcome | Currency | Derived | Unbounded | Interpret with uncertainty |
| return_on_investment | Net discounted value relative to discounted cost | Decision outcome | Proportion | Derived | Unbounded | Report calculation convention |
| simple_payback_years | Years to recover initial cost from annual net benefit | Decision outcome | Years | Derived | ≥ 0 or undefined | Does not discount cash flows |
