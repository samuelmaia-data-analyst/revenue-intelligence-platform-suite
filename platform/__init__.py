"""Core platform package.

This repository package is named ``platform``, which shadows Python's standard
library module with the same name. Third-party libs (for example, pandas)
import stdlib ``platform`` directly, so we proxy stdlib attributes here to keep
runtime compatibility when the project root is on ``PYTHONPATH``.
"""

from __future__ import annotations

import importlib.util
import sysconfig
from pathlib import Path

_STDLIB_PLATFORM_PATH = Path(sysconfig.get_paths()["stdlib"]) / "platform.py"
_SPEC = importlib.util.spec_from_file_location("_stdlib_platform", _STDLIB_PLATFORM_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"Unable to load stdlib platform module from {_STDLIB_PLATFORM_PATH}.")

_STDLIB_PLATFORM = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_STDLIB_PLATFORM)


def __getattr__(name: str):
    return getattr(_STDLIB_PLATFORM, name)
