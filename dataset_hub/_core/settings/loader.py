from typing import Any, Dict

from .default_settings import DEFAULT_SETTINGS
from .user_settings import RUNTIME_SETTINGS


def load_settings() -> Dict[str, Any]:
    return {**DEFAULT_SETTINGS, **RUNTIME_SETTINGS}
