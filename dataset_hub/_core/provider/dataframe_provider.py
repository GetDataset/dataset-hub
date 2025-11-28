from dataclasses import dataclass, field
from typing import Any, Dict

import pandas as pd

from dataset_hub._core.utils.pandas import read_dataframe

from .provider import (
    Provider,  # предполагается, что Provider в том же пакете
    ProviderConfig,
)


@dataclass
class DataFrameProviderConfig(ProviderConfig):
    """
    Configuration schema for `UrlProvider`.

    Attributes:
        url (str): HTTP(S) URL pointing to the dataset file.
        format (str): The format of the file (e.g., 'csv', 'parquet').
        read_kwargs (Dict[str, Any]): Optional keyword arguments forwarded
            directly to the corresponding pandas reader.
    """

    path_or_url: str
    format: str
    read_kwargs: Dict[str, Any] = field(default_factory=dict)


class DataFrameProvider(Provider[pd.DataFrame]):
    """
    Provider that loads a dataset from a remote URL and returns it as
    a pandas DataFrame.

    Regardless of the underlying file format, the output is always returned as:

        {"data": pandas.DataFrame}

    Supported formats depend on the implementation of `read_dataframe`.
    """

    ConfigClass = DataFrameProviderConfig

    def load(self) -> pd.DataFrame:
        """
        Fetch and load the dataset specified in the configuration.

        Returns:
            pd.DataFrame: The loaded pandas DataFrame.

        Raises:
            ValueError: If the file cannot be read or the format is unsupported.
        """
        df = read_dataframe(
            self.config["path_or_url"], self.config["format"], self.config["read_kwargs"]
        )

        return df
