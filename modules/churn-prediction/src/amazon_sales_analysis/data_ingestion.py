import sys
from importlib import import_module

sys.modules[__name__] = import_module("churn_prediction.data_ingestion")
