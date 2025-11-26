.. meta::
    :description lang=en:
        DatasetHub documentation: a unified interface for loading, managing, 
        and exploring machine learning datasets.


===============
DatasetHub
===============

**DatasetHub** is an educational project that provides a unified, simple API for loading
machine learning datasets via functions like ``.get_<dataset>()``:

.. code-block:: python

    import dataset_hub

    titanic = dataset_hub.classification.get_titanic()
    print(type(titanic))  # pandas.DataFrame


The goal is to make datasets easily accessible for beginners  
and provide a consistent interface for practitioners exploring many ML tasks.


What DatasetHub solves
######################

DatasetHub aims to remove the fragmentation around open data access:

- One unified API — ``.get_<dataset>()`` for any task (classification, regression, uplift, etc.).
- Simple entry point for students and beginners.
- Predictable structure across datasets.
- Easy way to explore open datasets with documented columns, targets, and descriptions.
- Potential to generate **synthetic realisitc datasets** (coming soon).


Available datasets
##################

See all supported datasets here: :ref:`datasets`

Or jump directly to some examples:

- :ref:`titanic`
- :ref:`iris`


Why this project exists
#######################

DatasetHub was created to unify the process of experimenting with ML datasets:

1. **Establish one API** for loading datasets across many ML tasks.
2. **Assemble a growing collection of open datasets**, well-documented and accessible.
3. **Provide realistic synthetic datasets** for tasks where open data is scarce  
   (fraud, churn, pricing, etc.).
4. Offer a clean educational layer for beginners.


Roadmap
#######

The project is evolving. Planned features:

- **Expansion of dataset collection with** additional datasets.
- **Addition of new data providers:** `sklearn`, `sklif`, `kaggle`, local CSV/Parquet support.
- **Configurable data sources + mirrors** (for stability and public availability).
- **Starter pack for contributors**, covering config creation, dataset structure, validation, logging.


Contributing
############

DatasetHub is experimental but actively growing.  
We welcome contributors of all experience levels.

- GitHub: https://github.com/getdataset/dataset-hub
- Open issues / ideas / dataset suggestions are highly appreciated.


API Disclaimer
##############

1. **External sources**  
   Some datasets depend on third-party hosts. If sources or mirrors temporarily fail,
   a ``get_<dataset>()`` function may stop working.  
   Please open an issue if you encounter persistent problems.

2. **Dynamic API**  
   If all public sources of a dataset permanently disappear, the dataset may be removed.

3. **Copyright**  
   Similar changes may occur if a copyright holder requests the removal of access to a dataset. If you are a copyright holder and want your dataset removed, contact us directly.


.. toctree::
   :hidden:

   self

.. toctree::
   :maxdepth: 2
   :caption: Contents

   install
   quick_start
   datasets/index
   dev_docs/index
