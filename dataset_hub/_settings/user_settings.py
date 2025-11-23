from typing import Any

RUNTIME_SETTINGS = {}

def set_option(key: str, value: Any) -> None: #TODO add validating keys and values
    RUNTIME_SETTINGS[key] = value