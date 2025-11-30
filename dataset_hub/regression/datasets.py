from typing import Optional

import pandas as pd

from dataset_hub._core.data_bundle import DataBundle
from dataset_hub._core.get_data import get_data as _get_data

task_type = "regression"


def get_housing(verbose: Optional[bool] = None) -> pd.DataFrame:
    """
    This is the dataset used in the second chapter of Aurélien Géron's
    recent book 'Hands-On Machine learning with Scikit-Learn and TensorFlow'.
    It serves as an excellent introduction to implementing machine learning algorithms
    because it requires rudimentary data cleaning, has an easily understandable
    list of variables and sits at an optimal size between being to toyish and
    too cumbersome.

    The data contains information from the 1990 California census. So although
    it may not help you with predicting current housing prices like the Zillow
    Zestimate dataset, it does provide an accessible introductory dataset for
    teaching people about the basics of machine learning.

    """
    dataset: DataBundle[pd.DataFrame] = _get_data(
        dataset_name="california_housing", task_type=task_type, verbose=verbose
    )
    return dataset["data"]
