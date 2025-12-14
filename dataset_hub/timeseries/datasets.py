from typing import Optional

import pandas as pd

from dataset_hub._core.data_bundle import DataBundle
from dataset_hub._core.get_data import get_data as _get_data

task_type = "timeseries"


def get_household_power(verbose: Optional[bool] = None) -> pd.DataFrame:
    """
    Load and return the Individual Household Electric Power Consumption dataset.

    Measurements of **electric power consumption in a single household** with a one-minute \
        sampling rate over a period of almost 4 years (December 2006 – November 2010). \
        Each record contains several electrical and sub-metering measurements.
     
    
    This dataset is designed for minute-level analysis of total household energy \
        consumption, capturing overall usage patterns of a single home.


    Original dataset: This dataset is available on the UCI Machine Learning \
        Repository:  
    `Individual Household Electric Power Consumption <https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption>`_

    Columns:

    - ``Date`` (str): Date of measurement in format dd/mm/yyyy
    - ``Time`` (str): Time of measurement in format hh:mm:ss
    - ``Global_active_power`` (float): Household global minute-averaged active \
        power (kilowatt)
    - ``Global_reactive_power`` (float): Household global minute-averaged reactive \
        power (kilowatt)
    - ``Voltage`` (float): Minute-averaged voltage (volt)
    - ``Sub_metering_1`` (float): Energy sub-metering No. 1 \
        (kitchen: dishwasher, oven, microwave; watt-hour of active energy)
    - ``Sub_metering_2`` (float): Energy sub-metering No. 2 \
        (laundry room: washing machine, tumble-drier, refrigerator, light; watt-hour)
    - ``Sub_metering_3`` (float): Energy sub-metering No. 3 \
        (electric water-heater, air-conditioner; watt-hour)
    - ``Global_intensity`` 🚩 (float): Household global minute-averaged current \
        intensity (ampere)

    Notes:
        - Missing values are present in approximately 1.25% of the rows. 
        - Active energy not covered by sub-meterings 1–3 can be calculated as: \
        ``(Global_active_power*1000/60 - Sub_metering_1 - Sub_metering_2 - Sub_metering_3)`` \
            in watt-hour.

    Args:
        verbose (bool, optional):
            If True, the function prints a link to the dataset documentation \
                in the log output after loading. (e.g., on this page)
            Default is None, which uses the global :ref:`settings`.

    Returns:
        pandas.DataFrame: The household power consumption dataset with all features.

    Quick Start:

    .. code-block:: python

        import dataset_hub

        household_power = dataset_hub.timeseries.get_household_power()

    """  # noqa

    dataset: DataBundle[pd.DataFrame] = _get_data(
        dataset_name="household_power", task_type=task_type, verbose=verbose
    )
    return dataset["data"]
