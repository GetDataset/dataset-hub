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
    
        import dataset_hub

        titanic = dataset_hub.classification.get_titanic()
    
    Baseline:
        
    .. code-block:: python

        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score
        from dataset_hub.classification import get_titanic

        # Get titanic dataset
        titanic = get_titanic()

        # Separate target variable (y) and features (X)
        y = titanic["survived"]
        X = titanic.drop("survived", axis=1)

        # Drop categorical columns for simplicity (you can preprocess them yourself)
        X = X.select_dtypes(include=["int64", "float64"])

        # Fill missing numeric values
        for col in X.columns:
            X[col] = X[col].fillna(X[col].median())

        # Split data into train and test parts
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Create and train the model
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", round(accuracy, 3))  # Example output: 0.706

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

        import dataset_hub

        iris = dataset_hub.classification.get_iris()

    Baseline:

    .. code-block:: python

        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score
        from dataset_hub.classification import get_iris

        # Get iris dataset
        iris = get_iris()

        # Separate target variable (y) and features (X)
        y = iris["species"]
        X = iris.drop("species", axis=1)

        # Split data into train and test parts
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Create and train the model
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", round(accuracy, 3))  # Example output: 0.967

    """
    dataset: DataBundle[pd.DataFrame] = _get_data(
        dataset_name="iris", task_type=task_type, verbose=verbose
    )
    return dataset["data"]
