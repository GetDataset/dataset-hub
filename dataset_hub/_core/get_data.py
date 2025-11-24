from typing import Dict, Any
from dataset_hub._core.provider import ProviderFactory
from dataset_hub._core.utils.config import ConfigFactory


def get_data(dataset_name: str, task_type: str) -> Dict[str, Any]:
    """
    Load a dataset and return it as a dictionary of tables (usually DataFrames).

    This is the main public API function of the library. It:
        1. Loads the dataset configuration.
        2. Instantiates the data provider.
        3. Loads the dataset using the data provider.

    Args:
        dataset_name (str): The name of the dataset (corresponding to the YAML config file).
        task_type (str): The type of task (e.g., "classification", "regression").

    Returns:
        Dict[str, pd.DataFrame]: A dictionary mapping table names to tables.

    Raises:
        FileNotFoundError: If the dataset configuration YAML file is not found.
        ValueError: If the provider type is unknown or misconfigured.
    """
    config = ConfigFactory.load_config(dataset_name, task_type)
    provider = ProviderFactory.build_provider(config["provider"])
    dataset = provider.load()

    return dataset