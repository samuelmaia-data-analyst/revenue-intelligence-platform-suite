import sys
from pathlib import Path

_MODULE_ROOT = Path(__file__).resolve().parents[2]
_REPO_PACKAGES = _MODULE_ROOT.parents[1] / "packages"
if str(_REPO_PACKAGES) not in sys.path:
    sys.path.insert(0, str(_REPO_PACKAGES))

from churn_prediction.config import PROJECT_ROOT

__version__ = "0.1.0"

__all__ = ["PROJECT_ROOT", "__version__"]
