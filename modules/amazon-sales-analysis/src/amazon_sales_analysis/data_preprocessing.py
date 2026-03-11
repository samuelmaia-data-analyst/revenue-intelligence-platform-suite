from pathlib import Path

import pandas as pd
from portfolio_analytics_shared.data_preprocessing import (
    clean_sales_data as _clean_sales_data,
)
from portfolio_analytics_shared.data_preprocessing import (
    load_raw_sales_data as _load_raw_sales_data,
)
from portfolio_analytics_shared.data_preprocessing import (
    save_processed_data as _save_processed_data,
)

from .config import PROCESSED_DATA_DIR, RAW_DATA_DIR

RAW_SUBDIR = "amazon_sales"
RAW_FILENAME = "amazon_sales_dataset.csv"
PROCESSED_FILENAME = "amazon_sales_clean.csv"


def load_raw_sales_data(raw_subdir: str = RAW_SUBDIR, filename: str = RAW_FILENAME) -> pd.DataFrame:
    return _load_raw_sales_data(raw_data_dir=RAW_DATA_DIR, raw_subdir=raw_subdir, filename=filename)


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    return _clean_sales_data(df)


def save_processed_data(df: pd.DataFrame, filename: str = PROCESSED_FILENAME) -> Path:
    return _save_processed_data(df, processed_data_dir=PROCESSED_DATA_DIR, filename=filename)
