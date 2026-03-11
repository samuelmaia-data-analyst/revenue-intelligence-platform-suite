from pathlib import Path

import pandas as pd

from .contracts import RAW_REQUIRED_COLUMNS


def load_raw_sales_data(*, raw_data_dir: Path, raw_subdir: str, filename: str) -> pd.DataFrame:
    source_path = raw_data_dir / raw_subdir / filename
    if not source_path.exists():
        raise FileNotFoundError(f"Arquivo bruto não encontrado: {source_path}")
    return pd.read_csv(source_path)


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    missing_columns = RAW_REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Colunas obrigatorias ausentes no dataset: {missing}")

    cleaned = df.copy()
    cleaned["order_date"] = pd.to_datetime(cleaned["order_date"], errors="coerce")

    numeric_columns = [
        "order_id",
        "product_id",
        "price",
        "discount_percent",
        "quantity_sold",
        "rating",
        "review_count",
        "discounted_price",
        "total_revenue",
    ]
    cleaned[numeric_columns] = cleaned[numeric_columns].apply(pd.to_numeric, errors="coerce")

    cleaned = cleaned.dropna(subset=["order_date", "price", "discount_percent", "quantity_sold"])
    cleaned = cleaned[(cleaned["quantity_sold"] > 0) & (cleaned["price"] >= 0)]
    cleaned["discount_percent"] = cleaned["discount_percent"].clip(lower=0, upper=100)
    cleaned["rating"] = cleaned["rating"].clip(lower=0, upper=5)

    cleaned["discounted_price"] = cleaned["price"] * (1 - cleaned["discount_percent"] / 100)
    cleaned["total_revenue"] = cleaned["discounted_price"] * cleaned["quantity_sold"]

    return cleaned.reset_index(drop=True)


def save_processed_data(df: pd.DataFrame, *, processed_data_dir: Path, filename: str) -> Path:
    output_path = processed_data_dir / filename
    df.to_csv(output_path, index=False)
    return output_path
