from typing import Callable

import pandas as pd
import pytest

from dataset_hub.classification.datasets import get_iris, get_titanic
from dataset_hub.regression.datasets import get_housing


@pytest.mark.parametrize(
    "func",
    [get_titanic, get_iris, get_housing],
)
def test_classification_datasets_smoke(func: Callable[[], pd.DataFrame]) -> None:
    df = func()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df.columns) > 0
