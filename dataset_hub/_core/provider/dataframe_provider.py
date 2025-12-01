from dataclasses import dataclass, field
from typing import Any, Callable, Dict

import pandas as pd

from .provider import (
    Provider,
    ProviderConfig,
)


@dataclass
class SourceConfig:
    """
    Configuration for data source.

    Attributes:
        type (str): Source type (e.g., 'url', 'file').
        url (str): URL or file path to the dataset.
        format (str): The format of the file (e.g., 'csv', 'parquet').
    """

    type: str
    url: str
    format: str


@dataclass
class DataFrameProviderConfig(ProviderConfig):
    """
    Configuration schema for DataFrameProvider.

    Attributes:
        source (Dict[str, Any] | SourceConfig): Source configuration with
            type, url, and format.
        read_kwargs (Dict[str, Any]): Optional keyword arguments forwarded
            directly to the corresponding pandas reader.
    """

    source: Dict[str, Any]
    read_kwargs: Dict[str, Any] = field(default_factory=dict)


class DataFrameProvider(Provider[pd.DataFrame]):
    """
    Provider that loads a dataset from a source (URL or file) and returns it as
    a pandas DataFrame.

    Regardless of the underlying file format, the output is always returned as:

        {"data": pandas.DataFrame}

    Supported formats depend on the implementation of `read_dataframe`.
    """

    ConfigClass = DataFrameProviderConfig

    # Registry of formats and corresponding pandas reader functions
    _READER_REGISTRY: Dict[str, Callable[..., pd.DataFrame]] = {
        "csv": pd.read_csv,
        "parquet": pd.read_parquet,
        "excel": pd.read_excel,
        "json": pd.read_json,
    }

    def load(self) -> pd.DataFrame:
        """
        Fetch and load the dataset specified in the configuration.

        Returns:
            pd.DataFrame: The loaded pandas DataFrame.

        Raises:
            ValueError: If the file cannot be read or the format is unsupported.
        """
        source = self.config["source"]
        source_type = source.get("type")
        
        if source_type != "url":
            raise ValueError(f"Source type '{source_type}' is not supported yet")

        url = source.get("url")
        if not url:
            raise ValueError("Source must contain 'url' key")

        format_ = source.get("format")
        if not format_:
            raise ValueError("Source must contain 'format' key")

        df = self.read_dataframe(
            url,
            format_,
            self.config.get("read_kwargs", {}),
        )

        return df

    def read_dataframe(
        self, path_or_url: str, format: str, read_kwargs: Dict[str, Any]
    ) -> pd.DataFrame:
        """
        Universal function to read a DataFrame from various file formats.

        Args:
            path_or_url (str): Local file path or URL to the data.
            format (str): Data format ('csv', 'parquet', 'excel', 'json').
            read_kwargs (dict, optional): Additional parameters to pass to
                the corresponding pandas reader function.

        Returns:
            pd.DataFrame: Loaded DataFrame.

        Raises:
            ValueError: If the specified format is not supported.
        """
        if read_kwargs is None:
            read_kwargs = {}

        format = format.lower()
        if format not in self._READER_REGISTRY:
            raise ValueError(
                f"Format '{format}' is not supported. "
                f"Supported formats: {list(self._READER_REGISTRY.keys())}"
            )

        reader = self._READER_REGISTRY[format]
        return reader(path_or_url, **read_kwargs)
