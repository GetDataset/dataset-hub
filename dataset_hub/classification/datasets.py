from typing import Any, Dict, Union

import pandas as pd

from dataset_hub._core.get_data import get_data

task_type = "classification"


def _get_data(dataset_name: str, **params) -> Union[Any, Dict[str, Any]]:
    """
    Load a dataset for the 'classification' task.

    This function provides a simple interface for users to load datasets
    relevant to the classification task.

    Args:
        dataset_name (str): Name of the dataset to load. Defaults to "titanic".
        **params: Additional parameters passed to the underlying loader (optional).

    Returns:
        Dict[str, Any]: A dictionary of tables (e.g., pandas DataFrames) corresponding
        to the dataset.
    """
    return get_data(dataset_name, task_type=task_type, **params)


def get_titanic(**params) -> pd.DataFrame:
    """
    Load and return the Titanic dataset (classification).

    A classic binary classification dataset containing information about
    passengers aboard the Titanic, including demographic and ticket-related features
    and survival outcome.

    Major columns:

    - ``survived`` (int): target variable, 1 if survived, 0 otherwise
    - ``pclass`` (int): passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)
    - ``sex`` (str): passenger gender
    - ``age`` (float): passenger age in years
    - ``sibsp`` (int): number of siblings/spouses aboard
    - ``parch`` (int): number of parents/children aboard
    - ``fare`` (float): ticket fare
    - ``embarked`` (str): port of embarkation (C = Cherbourg, Q = Queenstown
        , S = Southampton)

    Args:
        **params: Additional parameters passed to the underlying data loader.

    Returns:
        pandas.DataFrame: The Titanic dataset with all features including the target.

        - The DataFrame contains the columns listed above.
        - The target column is ``survived``.
        - All other columns can be used as features for classification tasks.

    Example::

        from dataset_hub.classification import get_titanic

        titanic = get_titanic()
        print(titanic.head())
        X = titanic.drop(columns=['survived'])
        y = titanic['survived']
    """
    return _get_data("titanic", **params)  # type: ignore[return-value]
