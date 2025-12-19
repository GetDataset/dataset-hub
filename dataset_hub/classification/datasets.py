from typing import Optional

import pandas as pd

from dataset_hub._core.data_bundle import DataBundle
from dataset_hub._core.get_data import get_data as _get_data

task_type = "classification"


def get_titanic(verbose: Optional[bool] = None) -> pd.DataFrame:
    """
    Load and return the Titanic dataset (classification).

    A classic binary classification dataset containing information about
    passengers aboard the Titanic, including demographic and ticket-related features
    and survival outcome.

    Original dataset: `Kaggle Titanic <https://www.kaggle.com/c/titanic/data>`_
    
    Columns:

    - ``pclass`` (int): passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)
    - ``name`` (str): full name of the passenger
    - ``sex`` (str): passenger gender
    - ``age`` (float): passenger age in years, may contain missing values
    - ``fare`` (float): ticket fare, may contain missing values
    - ``sibsp`` (int): number of siblings/spouses aboard
    - ``parch`` (int): number of parents/children aboard
    - ``survived`` 🚩 (int): **target variable**, 1 if survived, 0 otherwise

    Args:
        verbose (bool, optional):
            If True, the function prints a link to the dataset documentation in \
            the log output after loading. (e.g., on this page)
            Default is None, which uses the global :ref:`settings`.

    Returns:
        pandas.DataFrame: The Titanic dataset with all features including the target.
        
    Quick Start:

    .. code-block:: python
    
        from dataset_hub.classification import get_titanic

        df = get_titanic()

    """
    dataset: DataBundle[pd.DataFrame] = _get_data(
        dataset_name="titanic", task_type=task_type, verbose=verbose
    )
    return dataset["data"]


def get_iris(verbose: Optional[bool] = None) -> pd.DataFrame:
    """
    Load and return the Iris dataset (classification).

    A classic multiclass classification dataset containing measurements
    of iris flowers from three different species.

    Original dataset: `UCI Iris <https://archive.ics.uci.edu/ml/datasets/iris>`_

    Columns:

    - ``sepal_length`` (float): length of the sepal in cm
    - ``sepal_width`` (float): width of the sepal in cm
    - ``petal_length`` (float): length of the petal in cm
    - ``petal_width`` (float): width of the petal in cm
    - ``species`` 🚩 (str): **target variable**, species name (setosa, \
        versicolor, virginica)

    Args:
        verbose (bool, optional):
            If True, the function prints a link to the dataset documentation \
                in the log output after loading. (e.g., on this page)
            Default is None, which uses the global :ref:`settings`.

    Returns:
        pandas.DataFrame: The Iris dataset with all features including the target.

    Quick Start:

    .. code-block:: python

        from dataset_hub.classification import get_iris

        df = get_iris()

    """
    dataset: DataBundle[pd.DataFrame] = _get_data(
        dataset_name="iris", task_type=task_type, verbose=verbose
    )
    return dataset["data"]
