from typing import Optional

import pandas as pd

from dataset_hub._core.data_bundle import DataBundle
from dataset_hub._core.get_data import get_data as _get_data

task_type = "regression"


def get_housing(verbose: Optional[bool] = None) -> pd.DataFrame:
    """
    Load and return the California Housing dataset (regression).

    Median house prices for California districts derived from the 1990 census.

    This dataset is intended for **predicting median housing values at the block \
        level**, reflecting broader economic and social patterns rather than \
        individual home prices. Each record summarizes features of a block, such \
        as population, total rooms, and median income, making it suitable for \
        regional-level regression tasks.
    
    Original dataset: This dataset was used in Aurélien Géron's book \
        'Hands-On Machine Learning with Scikit-Learn and TensorFlow'. \
        `California Housing on Kaggle <https://www.kaggle.com/camnugent/california-housing-prices>`_

    Columns:

    - ``longitude`` (float): a measure of how far west a house is; higher is farther\
          west
    - ``latitude`` (float): a measure of how far north a house is; higher is farther\
          north
    - ``housing_median_age`` (float): median age of a house within a block; lower \
        is newer
    - ``total_rooms`` (int): total number of rooms within a block
    - ``total_bedrooms`` (int): total number of bedrooms within a block
    - ``population`` (int): total number of people residing within a block
    - ``households`` (int): total number of households within a block
    - ``median_income`` (float): median income for households in tens of thousands \
        of USD
    - ``ocean_proximity`` (str): location of the house with respect to ocean/sea
    - ``median_house_value`` 🚩 (float): median house value in USD

    Args:
        verbose (bool, optional):
            If True, the function prints a link to the dataset documentation \
                in the log output after loading. (e.g., on this page)
            Default is None, which uses the global :ref:`settings`.

    Returns:
        pandas.DataFrame: The California Housing dataset with all features \
            including the target.

    Quick Start:

    .. code-block:: python

        import dataset_hub

        housing = dataset_hub.regression.get_housing()

    Baseline:

    .. code-block:: python

        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error
        from dataset_hub.regression import get_housing

        # Get housing dataset
        housing = get_housing()

        # Separate target variable (y) and features (X)
        y = housing["median_house_value"]
        X = housing.drop("median_house_value", axis=1)

        # Drop categorical columns for simplicity (you can preprocess them yourself)
        X = X.select_dtypes(include=["int64", "float64"])

        # Fill missing numeric values
        for col in X.columns:
            X[col] = X[col].fillna(X[col].median())

        # Split data into train and test parts
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Create and train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Calculate RMSE
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        print("RMSE:", round(rmse, 2))  # Example output: 69000.53

    """

    dataset: DataBundle[pd.DataFrame] = _get_data(
        dataset_name="california_housing", task_type=task_type, verbose=verbose
    )
    return dataset["data"]
