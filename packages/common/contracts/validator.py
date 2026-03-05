from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SCHEMA_TYPE_MAP = {
    "string": str,
    "number": (int, float),
    "integer": int,
    "boolean": bool,
    "object": dict,
    "array": list,
}


def _schemas_dir() -> Path:
    return Path(__file__).resolve().parent


def load_schema(schema_file_name: str) -> dict[str, Any]:
    schema_path = _schemas_dir() / schema_file_name
    with schema_path.open("r", encoding="utf-8") as fp:
        return json.load(fp)


def validate_contract(payload: dict[str, Any], schema_file_name: str) -> list[str]:
    schema = load_schema(schema_file_name)
    errors: list[str] = []

    if schema.get("type") != "object":
        return ["Only object schemas are supported by this validator."]
    if not isinstance(payload, dict):
        return ["Payload is not an object."]

    required = schema.get("required", [])
    properties = schema.get("properties", {})

    for key in required:
        if key not in payload:
            errors.append(f"Missing required key: {key}")

    for key, rule in properties.items():
        if key not in payload:
            continue
        expected_type = rule.get("type")
        if expected_type not in SCHEMA_TYPE_MAP:
            errors.append(f"Unsupported type '{expected_type}' for key '{key}'")
            continue
        if not isinstance(payload[key], SCHEMA_TYPE_MAP[expected_type]):
            errors.append(
                f"Invalid type for '{key}': expected {expected_type}, got {type(payload[key]).__name__}"
            )

    return errors
