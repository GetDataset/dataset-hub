.. _quick_start:

**********
Quick Start
**********


This section shows how to load your first dataset using the unified
``.get_<dataset>()`` API.

Basic example
-------------

Load any available dataset in one line:

.. code-block:: python

    import dataset_hub

    titanic = dataset_hub.classification.get_titanic()
    print(type(titanic))  # pandas.DataFrame

Available datasets
------------------

See the full list here: :ref:`datasets`

Or jump directly to the quick examples:

- :ref:`titanic`
- :ref:`iris`

Next steps
----------

You can now explore the dataset, run preprocessing, or build your first model.
DatasetHub keeps all datasets accessible through a single, simple interface.