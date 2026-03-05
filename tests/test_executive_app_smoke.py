from __future__ import annotations

import py_compile
from pathlib import Path


def test_executive_app_files_compile() -> None:
    root = Path(__file__).resolve().parents[1]
    files = [
        root / "apps" / "executive-dashboard" / "app.py",
        root / "apps" / "executive-dashboard" / "pages" / "1_Executive_KPI_Board.py",
        root / "apps" / "executive-dashboard" / "pages" / "2_Modules_Access.py",
    ]
    for file_path in files:
        py_compile.compile(str(file_path), doraise=True)
