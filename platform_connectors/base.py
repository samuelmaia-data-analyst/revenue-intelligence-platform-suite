from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import pandas as pd


class TelemetryConnector(ABC):
    """Standard connector interface for enterprise telemetry sources."""

    @abstractmethod
    def fetch_monthly_revenue_telemetry(self) -> pd.DataFrame:
        """Return monthly revenue telemetry with NRR and churn metrics."""

    @abstractmethod
    def fetch_latest_kpis(self) -> dict[str, Any]:
        """Return a latest KPI snapshot for executive consumption."""
