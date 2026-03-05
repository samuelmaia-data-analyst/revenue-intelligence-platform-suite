from __future__ import annotations

import json
from pathlib import Path

from common.contracts import validate_contract


def test_showcase_summary_contract_is_valid() -> None:
    root = Path(__file__).resolve().parents[1]
    summary_path = root / "reports" / "showcase" / "summary.json"
    assert summary_path.exists(), "Missing showcase summary artifact."

    with summary_path.open("r", encoding="utf-8") as fp:
        summary = json.load(fp)

    errors = validate_contract(summary, "showcase_summary.schema.json")
    assert not errors, f"Showcase summary contract errors: {errors}"


def test_action_adoption_event_contract_is_valid() -> None:
    event = {
        "action_id": "CUST-100::Executive Save Offer",
        "timestamp": "2026-03-05T00:00:00Z",
        "outcome": "accepted",
        "metadata": {"owner": "CSM Team A"},
    }
    errors = validate_contract(event, "action_adoption_event.schema.json")
    assert not errors, f"Action adoption contract errors: {errors}"
