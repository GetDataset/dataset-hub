import pandas as pd

from ._get_data import _get_data


def get_titanic(**params) -> pd.DataFrame:
    return _get_data("titanic", **params)  # type: ignore[return-value]
