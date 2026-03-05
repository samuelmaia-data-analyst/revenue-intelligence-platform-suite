from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from platform_observability import ActionAdoptionLogger


def test_action_adoption_logger_writes_csv_and_jsonl(tmp_path: Path) -> None:
    logger = ActionAdoptionLogger(tmp_path)
    event = logger.log(
        action_id="CUST-100::Executive Save Offer",
        outcome="accepted",
        metadata={"owner": "CSM Team A"},
    )

    csv_path = tmp_path / "action_adoption_log.csv"
    jsonl_path = tmp_path / "action_adoption_log.jsonl"
    assert csv_path.exists()
    assert jsonl_path.exists()
    assert event["action_id"] == "CUST-100::Executive Save Offer"

    csv_df = pd.read_csv(csv_path)
    assert csv_df.iloc[0]["outcome"] == "accepted"

    with jsonl_path.open("r", encoding="utf-8") as fp:
        lines = [json.loads(line) for line in fp if line.strip()]
    assert lines[0]["metadata"]["owner"] == "CSM Team A"
