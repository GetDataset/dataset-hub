from typing import Optional

import pandas as pd

from dataset_hub._core.dataset import Dataset
from dataset_hub._core.get_data import get_data as _get_data

task_type = "classification"


def get_titanic(verbose: Optional[bool] = None) -> pd.DataFrame:
    """
    Load and return the Titanic dataset (classification).

    A classic binary classification dataset containing information about
    passengers aboard the Titanic, including demographic and ticket-related features
    and survival outcome.

    Columns:

    - ``survived`` (int): target variable, 1 if survived, 0 otherwise
    - ``pclass`` (int): passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)
    - ``name`` (str): full name of the passenger
    - ``sex`` (str): passenger gender
    - ``age`` (float): passenger age in years
    - ``fare`` (float): ticket fare
    - ``sibsp`` (int): number of siblings/spouses aboard
    - ``parch`` (int): number of parents/children aboard

    Args:
        **params: Additional parameters passed to the underlying data loader
            (see :ref:`get_data` for details).

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
    dataset: Dataset[pd.DataFrame] = _get_data(
        dataset_name="titanic", task_type=task_type, verbose=verbose
    )
    return dataset["data"]


def get_iris(verbose: Optional[bool] = None) -> pd.DataFrame:
    """
    Load and return the Iris dataset (classification).

    A classic multiclass classification dataset containing measurements
    of iris flowers from three different species.

    Columns:

    - ``sepal_length`` (float): length of the sepal in cm
    - ``sepal_width`` (float): width of the sepal in cm
    - ``petal_length`` (float): length of the petal in cm
    - ``petal_width`` (float): width of the petal in cm
    - ``species`` (str): target variable, species name (setosa, versicolor, virginica)

    Args:
        **params: Additional parameters passed to the underlying data loader
            (see :ref:`get_data` for details).

    Returns:
        pandas.DataFrame: The Iris dataset with all features including the target.

        - The DataFrame contains the columns listed above.
        - The target column is ``species``.
        - All other columns can be used as features for classification tasks.

    Example::

        from dataset_hub.classification import get_iris

        iris = get_iris()
        print(iris.head())
        X = iris.drop(columns=['species'])
        y = iris['species']
    """
    dataset: Dataset[pd.DataFrame] = _get_data(
        dataset_name="iris", task_type=task_type, verbose=verbose
    )
    return dataset["data"]
