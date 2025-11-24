from typing import Any, Dict

from dataset_hub._core.get_data import get_data as _get_data
from dataset_hub._core.utils.paths import list_available_datasets

task_type = "classification"


def get_data(dataset_name: str = "titanic", **params) -> Dict[str, Any]:
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

    Raises:
        ValueError: If the specified dataset_name is not among the available datasets.

    Examples:
        >>> import dataset_hub
        >>> dataset = dataset_hub.classification.get_data("titanic")
        >>> type(data)
        <class 'dict'>
        >>> data.keys()
        dict_keys(['data'])
        >>> df = data['data']
        >>> df.head()
    """
    allowed = list_available_datasets(task_type=task_type)

    if dataset_name not in allowed:
        raise ValueError(f"Unknown dataset '{dataset_name}'. Allowed: {allowed}")

    return _get_data(dataset_name, task_type=task_type, **params)
