import pandas as pd
from portfolio_analytics_shared.visualization import (
    sales_trend_over_time as _sales_trend_over_time,
)
from portfolio_analytics_shared.visualization import (
    top_categories_by_sales as _top_categories_by_sales,
)

from .config import FIGURES_DIR


def sales_trend_over_time(df: pd.DataFrame) -> None:
    _sales_trend_over_time(df, figures_dir=FIGURES_DIR)


def top_categories_by_sales(df: pd.DataFrame, top_n: int = 10) -> None:
    _top_categories_by_sales(df, figures_dir=FIGURES_DIR, top_n=top_n)
