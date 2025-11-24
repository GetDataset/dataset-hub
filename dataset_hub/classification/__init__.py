from dataset_hub._core.get_data import get_data as _get_data
from dataset_hub._core.utils.paths import list_available_datasets
from typing import Any, Dict

task_type = "classification"


def get_data(dataset_name: str = "titanic", **params) -> Dict[str, Any]:
    allowed = list_available_datasets(task_type=task_type)

    if dataset_name not in allowed:
        raise ValueError(f"Unknown dataset '{dataset_name}'. Allowed: {allowed}")

    return _get_data(dataset_name, task_type=task_type, **params)
