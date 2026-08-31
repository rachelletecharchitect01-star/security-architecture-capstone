"""Starter decision model for the security-architecture capstone.

Replace illustrative inputs only after documenting them in the assumption register.
The script intentionally fails when required inputs are absent so placeholder
values cannot be mistaken for results.
"""

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "analysis" / "outputs"


@dataclass(frozen=True)
class ModelInputs:
    annual_incident_probability: float
    expected_consequence: float
    control_effectiveness: float
    initial_cost: float
    annual_operating_cost: float
    time_horizon_years: int
    discount_rate: float


def validate_inputs(inputs: ModelInputs) -> None:
    proportions = {
        "annual_incident_probability": inputs.annual_incident_probability,
        "control_effectiveness": inputs.control_effectiveness,
        "discount_rate": inputs.discount_rate,
    }
    for name, value in proportions.items():
        if not 0 <= value <= 1:
            raise ValueError(f"{name} must be between 0 and 1.")

    if inputs.expected_consequence < 0:
        raise ValueError("expected_consequence cannot be negative.")
    if inputs.initial_cost <= 0:
        raise ValueError("initial_cost must be positive.")
    if inputs.annual_operating_cost < 0:
        raise ValueError("annual_operating_cost cannot be negative.")
    if inputs.time_horizon_years < 1:
        raise ValueError("time_horizon_years must be at least 1.")


def evaluate_investment(inputs: ModelInputs) -> dict[str, float]:
    validate_inputs(inputs)

    baseline_loss = (
        inputs.annual_incident_probability * inputs.expected_consequence
    )
    residual_loss = baseline_loss * (1 - inputs.control_effectiveness)
    annual_avoided_loss = baseline_loss - residual_loss
    annual_net_benefit = annual_avoided_loss - inputs.annual_operating_cost

    years = np.arange(1, inputs.time_horizon_years + 1)
    discount_factors = 1 / ((1 + inputs.discount_rate) ** years)
    pv_operating_costs = float(
        np.sum(inputs.annual_operating_cost * discount_factors)
    )
    pv_benefits = float(np.sum(annual_avoided_loss * discount_factors))
    pv_costs = inputs.initial_cost + pv_operating_costs
    npv = pv_benefits - pv_costs
    roi = npv / pv_costs

    payback = (
        inputs.initial_cost / annual_net_benefit
        if annual_net_benefit > 0
        else np.inf
    )

    return {
        "baseline_expected_annual_loss": baseline_loss,
        "residual_expected_annual_loss": residual_loss,
        "expected_annual_avoided_loss": annual_avoided_loss,
        "present_value_benefits": pv_benefits,
        "present_value_costs": pv_costs,
        "net_present_value": npv,
        "return_on_investment": roi,
        "simple_payback_years": payback,
    }


def main() -> None:
    raise SystemExit(
        "No analysis was run. Qualify the data and replace this guard with "
        "documented ModelInputs before generating results."
    )


if __name__ == "__main__":
    main()
