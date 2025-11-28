from typing import Callable

import pandas as pd
import pytest

from dataset_hub.classification import datasets


@pytest.mark.parametrize(
    "func",
    [
        datasets.get_titanic,
        datasets.get_iris,
    ],
)
def test_classification_datasets_smoke(func: Callable[[], pd.DataFrame]) -> None:
    df = func()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df.columns) > 0
