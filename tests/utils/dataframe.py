import pandas as pd


def check_dataframe(df: pd.DataFrame) -> None:
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert len(df.columns) > 0
