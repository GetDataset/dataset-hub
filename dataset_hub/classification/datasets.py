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
    return _get_data("titanic", **params)  # type: ignore[return-value]


def get_iris(**params) -> pd.DataFrame:
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

    return _get_data("iris", **params)  # type: ignore[return-value]

def get_breast_cancer(**params) -> pd.DataFrame:
    """
    Load and return the Breast Cancer Wisconsin dataset (classification).

    A classic binary classification dataset containing features computed
    from breast tissue samples and the target indicating whether a tumor
    is malignant or benign.

    Columns:

    - ``Id`` (int): unique identifier for the sample
    - ``Cl.thickness`` (int): clump thickness
    - ``Cell.size`` (int): uniformity of cell size
    - ``Cell.shape`` (int): uniformity of cell shape
    - ``Marg.adhesion`` (int): marginal adhesion
    - ``Epith.c.size`` (int): epithelial cell size
    - ``Bare.nuclei`` (float): bare nuclei count
    - ``Bl.cromatin`` (int): bland chromatin
    - ``Normal.nucleoli`` (int): normal nucleoli
    - ``Mitoses`` (int): mitoses count
    - ``Class`` (int): target variable, 0 for benign, 1 for malignant

    Args:
        **params: Additional parameters passed to the underlying data loader
            (see :ref:`get_data` for details).

    Returns:
        pandas.DataFrame: The Breast Cancer dataset with all features including the target.

        - The DataFrame contains the columns listed above.
        - The target column is ``Class``.
        - All other columns can be used as features for classification tasks.

    Example::

        from dataset_hub.classification import get_breast_cancer

        breast_cancer = get_breast_cancer()
        print(breast_cancer.head())
        X = breast_cancer.drop(columns=['Class'])
        y = breast_cancer['Class']
    """
    return _get_data("breast_cancer", **params)  # type: ignore[return-value]
