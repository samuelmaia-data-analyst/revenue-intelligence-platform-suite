import pandas as pd
from portfolio_analytics_shared.eda import basic_eda as _basic_eda

from churn_prediction.config import FIGURES_DIR


def basic_eda(df: pd.DataFrame) -> None:
    _basic_eda(df, figures_dir=FIGURES_DIR)
