import pandas as pd
from .provider import ProviderConfig
from typing import Dict, Any
from dataclasses import dataclass, field, asdict
from urllib.parse import urlparse
from .provider import Provider  # предполагается, что Provider в том же пакете
from dataset_hub._core.utils.pandas import read_dataframe


@dataclass
class UrlProviderConfig(ProviderConfig):
    """
    Configuration for UrlProvider.

    Attributes:
        url (str): The URL from which to load the dataset.
        format (str): The format of the file (e.g., 'csv', 'parquet').
        read_kwargs (Dict[str, Any]): Optional keyword arguments to pass to the pandas read function.
    """
    url: str
    format: str
    read_kwargs: Dict[str, Any] = field(default_factory=dict)


class UrlProvider(Provider):
    """
    Provider that loads a dataset from a URL and returns a pandas DataFrame.

    This provider always returns a DataFrame regardless of file format.
    """

    def load(self) -> Dict[str, Any]:
        """
        Load the dataset from the configured URL and return it as a DataFrame.

        Returns:
            Dict[str, Any]: The loaded dataset object, wrapping a pandas DataFrame.
        """
        url = self.config["url"]
        file_format = self.config["format"]
        read_kwargs = self.config["read_kwargs"]

        data = read_dataframe(url, file_format, read_kwargs)

        dataset = {}
        dataset["data"] = data

        return dataset


    def _prepare_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate and normalize the configuration dictionary using config dataclass.

        Args:
            config (Dict[str, Any]): The raw configuration dictionary.

        Returns:
            Dict[str, Any]: The validated and normalized configuration.
        """
        try:
            config = asdict(UrlProviderConfig(**config))
        except TypeError as e:
            raise ValueError(f"Invalid UrlProvider config: {e}")
        return config