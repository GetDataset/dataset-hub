.. |colab_button| image:: https://colab.research.google.com/assets/colab-badge.svg
   :alt: Open In Colab
   :target: https://colab.research.google.com/github/GetDataset/dataset-hub/blob/main/notebooks/quick_start/classification/titanic.ipynb
.. _quick_start:

**************
Quick Start
**************


This section shows how to load your first dataset using the unified
``get_<dataset>()`` API.

Basic example
-------------

Load any dataset in a familiar format (e.g., a pandas DataFrame) with a single function call:

.. code-block:: python

    import dataset_hub

    dataset = dataset_hub.classification.get_titanic() # pd.DataFrame
    
After calling the function, a link to the dataset page will appear in the log output.
It contains detailed information about the dataset (description, columns, target, etc.).

Next steps
----------

You can proceed in two ways:

    - Start your own experiments with the dataset (split into train and test, build validation, perform feature engineering, build models, etc.)
    - Use a ready-made baseline provided in the documentation. For example, here is a simple baseline for Titanic: |colab_button|

Available datasets
------------------

See the full list here: :ref:`datasets`

Or jump directly to the quick examples:

- :ref:`titanic`
- :ref:`iris`
- :ref:`california_housing`
- :ref:`household_power`

