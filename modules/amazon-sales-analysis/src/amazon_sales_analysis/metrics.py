from __future__ import annotations

from pathlib import Path

import pandas as pd
from portfolio_analytics_shared.metrics import (
    PRODUCT_METRICS_VERSION as _PRODUCT_METRICS_VERSION,
)
from portfolio_analytics_shared.metrics import (
    collect_product_metrics as _collect_product_metrics,
)
from portfolio_analytics_shared.metrics import (
    save_product_metrics as _save_product_metrics,
)

from .config import METRICS_DIR

PRODUCT_METRICS_VERSION = _PRODUCT_METRICS_VERSION


def collect_product_metrics(
    df_raw: pd.DataFrame,
    df_clean: pd.DataFrame,
    df_featured: pd.DataFrame,
    *,
    contract_version: str,
) -> dict[str, float | int | str]:
    return _collect_product_metrics(
        df_raw,
        df_clean,
        df_featured,
        contract_version=contract_version,
    )


def save_product_metrics(
    metrics: dict[str, float | int | str], output_path: Path | None = None
) -> Path:
    return _save_product_metrics(metrics, metrics_dir=METRICS_DIR, output_path=output_path)
