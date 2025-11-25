from typing import Any, Dict, Union

import pandas as pd

from dataset_hub._core.get_data import get_data

task_type = "classification"


def _get_data(dataset_name: str, **params) -> Union[Any, Dict[str, Any]]:
    """
    Load a dataset for the 'classification' task.

    This function provides a simple interface for users to load datasets
    relevant to the classification task.

    Args:
        dataset_name (str): Name of the dataset to load. Defaults to "titanic".
        **params: Additional parameters passed to the underlying loader (optional).

    Returns:
        Dict[str, Any]: A dictionary of tables (e.g., pandas DataFrames) corresponding
        to the dataset.
    """
    return get_data(dataset_name, task_type=task_type, **params)


def get_titanic(**params) -> pd.DataFrame:
    return _get_data("titanic", **params)  # type: ignore[return-value]
