.. meta::
    :description lang=en:
        DatasetHub documentation: a unified interface for loading, managing, 
        and exploring machine learning datasets.


===============
DatasetHub
===============

**DatasetHub** provides a unified, simple API for loading machine learning datasets  
through functions like ``get_<dataset>()`` — all returned in familiar formats.

.. note::

   New here? Start with the :ref:`quick_start` to load your first dataset.

The goal is to remove unnecessary friction when exploring new ML tasks  
and give both beginners and practitioners a consistent, predictable way  
to access well-documented datasets with ready-to-run baselines.


What DatasetHub solves
######################

Working with open datasets is often harder than it should be.  
DatasetHub reduces this overhead by offering:

- **One unified API** — ``get_<dataset>()`` for any supported task.
- **Easy entry point** for students and beginners.
- **Detailed documentation** with descriptions, sources, and examples.
- **Consistent structure** across datasets (columns, target, metadata, baseline).
- **Starter baselines** so you can experiment immediately.

Supported datasets
##################

See all supported datasets here: :ref:`datasets`

Or jump directly to the quick examples:

- :ref:`titanic`
- :ref:`iris`
- :ref:`california_housing`
- :ref:`household_power`


.. toctree::
   :hidden:

   self

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents

   install
   quick_start
   datasets/index
   dev_docs/index
