from __future__ import annotations

from pathlib import Path

import pandas as pd

from platform_connectors import SQLiteTelemetryConnector, seed_demo_telemetry


def test_sqlite_connector_reads_seeded_telemetry(tmp_path: Path) -> None:
    db_path = tmp_path / "enterprise_telemetry.sqlite"
    monthly = pd.DataFrame(
        [
            {"month": "2026-01", "SALES": 100000.0},
            {"month": "2026-02", "SALES": 110000.0},
        ]
    )
    seed_demo_telemetry(db_path, monthly)

    connector = SQLiteTelemetryConnector(db_path)
    telemetry = connector.fetch_monthly_revenue_telemetry()
    latest = connector.fetch_latest_kpis()

    assert len(telemetry) == 2
    assert {"month", "revenue_usd", "nrr", "gross_churn"}.issubset(telemetry.columns)
    assert latest["latest_month"] == "2026-02"
    assert latest["latest_revenue_usd"] == 110000.0
