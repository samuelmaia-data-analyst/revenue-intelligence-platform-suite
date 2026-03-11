from pathlib import Path

from portfolio_analytics_shared.data_ingestion import (
    download_amazon_sales_dataset as _download_amazon_sales_dataset,
)

from churn_prediction.config import KAGGLE_DATASET, RAW_DATA_DIR

RAW_SUBDIR = "amazon_sales"
RAW_FILENAME = "amazon_sales_dataset.csv"


def download_amazon_sales_dataset() -> Path:
    return _download_amazon_sales_dataset(
        raw_data_dir=RAW_DATA_DIR,
        kaggle_dataset=KAGGLE_DATASET,
        raw_subdir=RAW_SUBDIR,
        raw_filename=RAW_FILENAME,
    )
