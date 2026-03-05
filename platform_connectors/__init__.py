"""Runtime-safe telemetry connectors (avoids stdlib `platform` name collision)."""

from .base import TelemetryConnector
from .sqlite import SQLiteTelemetryConnector, seed_demo_telemetry

__all__ = ["TelemetryConnector", "SQLiteTelemetryConnector", "seed_demo_telemetry"]
