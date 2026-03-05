from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd


class ActionAdoptionLogger:
    """Writes action adoption events in CSV and JSONL for showcase observability."""

    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        self.csv_path = output_dir / "action_adoption_log.csv"
        self.jsonl_path = output_dir / "action_adoption_log.jsonl"

    def log(self, action_id: str, outcome: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        event = {
            "action_id": action_id,
            "timestamp": pd.Timestamp.utcnow().isoformat(),
            "outcome": outcome,
            "metadata": metadata or {},
        }
        self._append_csv(event)
        self._append_jsonl(event)
        return event

    def _append_csv(self, event: dict[str, Any]) -> None:
        record = pd.DataFrame(
            [
                {
                    "action_id": event["action_id"],
                    "timestamp": event["timestamp"],
                    "outcome": event["outcome"],
                    "metadata_json": json.dumps(event["metadata"], ensure_ascii=True),
                }
            ]
        )
        header = not self.csv_path.exists()
        record.to_csv(self.csv_path, mode="a", index=False, header=header)

    def _append_jsonl(self, event: dict[str, Any]) -> None:
        with self.jsonl_path.open("a", encoding="utf-8") as fp:
            fp.write(json.dumps(event, ensure_ascii=True) + "\n")
