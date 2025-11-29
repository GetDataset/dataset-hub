from typing import Callable

import pandas as pd
import pytest

from tests.datasets import AVAILABILITY_DATAFRAME_DATASETS
from tests.utils.dataframe import check_dataframe


@pytest.mark.parametrize("dataset_func", AVAILABILITY_DATAFRAME_DATASETS)
def test_availability_dataframes(dataset_func: Callable[[], pd.DataFrame]) -> None:
    df = dataset_func()
    check_dataframe(df)
