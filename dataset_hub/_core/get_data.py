from typing import Any, Dict, Optional, Union

from dataset_hub._core.provider import ProviderFactory
from dataset_hub._core.utils.config import ConfigFactory
from dataset_hub._core.utils.logger import log_dataset_doc_doc_link


@log_dataset_doc_doc_link()
def get_data(
    dataset_name: str, task_type: str, verbose: Optional[bool] = None
) -> Union[Any, Dict[str, Any]]:
    """
    Core backend function used by all `.get_<dataset_name>()` functions to load \
        datasets.

    This function:
        1. Loads the dataset configuration using :ref:`ConfigFactory`.
        2. Instantiates the appropriate Provider via :ref:`ProviderFactory`.
        3. Loads the dataset using :ref:`providers`.
        4. ``(optional)`` Logs a link to the dataset documentation once per session \
            if verbose is enabled (either via argument or :ref:`settings`).

    Args:
        dataset_name (str): The name of the dataset (corresponding to the \
            YAML config file).
        task_type (str): The type of task (e.g., "classification", "regression").
        verbose (bool, optional): Whether to print dataset information and \
            documentation link. If None, the global library setting is used.

    Returns:
        Union[Any, Dict[str, Any]]: Either a single object (`Any`) or a dictionary \
            mapping table names to objects. Most commonly, `Any` is:

        - If a table: typically a `pd.DataFrame`, unless a specific reader or provider \
            returns another type. 
        - Could also be other ML data entities, e.g., graphs, arrays, etc.
            
    Raises:
        FileNotFoundError: If the dataset configuration YAML file is not found.
        ValueError: If the provider type is unknown or misconfigured.
    """
    config = ConfigFactory.load_config(dataset_name, task_type)
    provider = ProviderFactory.build_provider(config["provider"])
    dataset = provider.load()

    return dataset
