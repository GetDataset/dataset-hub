import pandas as pd
from typing import Any, Dict, Callable

# Registry of formats and corresponding pandas reader functions
READERS: Dict[str, Callable] = {
    "csv": pd.read_csv,
    "parquet": pd.read_parquet,
    "excel": pd.read_excel,
    "json": pd.read_json
}

def read_dataframe(path_or_url: str, format: str, read_kwargs: Dict[str, Any] = None) -> pd.DataFrame:
    """
    Universal function to read a DataFrame from various file formats.

    Args:
        path_or_url (str): Local file path or URL to the data.
        format (str): Data format ('csv', 'parquet', 'excel', 'json').
        read_kwargs (dict, optional): Additional parameters to pass to the corresponding pandas reader function.

    Returns:
        pd.DataFrame: Loaded DataFrame.

    Raises:
        ValueError: If the specified format is not supported.
    """
    if read_kwargs is None:
        read_kwargs = {}

    format = format.lower()
    if format not in READERS:
        raise ValueError(f"Format '{format}' is not supported. Supported formats: {list(READERS.keys())}")

    reader = READERS[format]
    return reader(path_or_url, **read_kwargs)
