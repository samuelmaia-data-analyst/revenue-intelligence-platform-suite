from pathlib import Path

import pandas as pd
from portfolio_analytics_shared.contracts import (
    RAW_REQUIRED_COLUMNS as _RAW_REQUIRED_COLUMNS,
)
from portfolio_analytics_shared.contracts import DataContractResult
from portfolio_analytics_shared.contracts import (
    enforce_raw_contract as _enforce_raw_contract,
)
from portfolio_analytics_shared.contracts import (
    export_contract_snapshot as _export_contract_snapshot,
)
from portfolio_analytics_shared.contracts import (
    validate_raw_contract as _validate_raw_contract,
)

from churn_prediction.config import CONTRACTS_DIR

RAW_REQUIRED_COLUMNS = _RAW_REQUIRED_COLUMNS


def validate_raw_contract(df: pd.DataFrame) -> DataContractResult:
    return _validate_raw_contract(df)


def enforce_raw_contract(df: pd.DataFrame) -> None:
    _enforce_raw_contract(df)


def export_contract_snapshot(*, contract_version: str, output_path: Path | None = None) -> Path:
    return _export_contract_snapshot(
        contract_version=contract_version,
        contracts_dir=CONTRACTS_DIR,
        output_path=output_path,
    )
