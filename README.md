[![PyPI version](https://img.shields.io/pypi/v/dataset-hub.svg)](https://pypi.org/project/dataset-hub/)
[![Docs](https://img.shields.io/badge/docs-dataset?label=dataset-hub)](https://getdataset.github.io/dataset-hub/index.html)

# DatasetHub: Instant ML datasets with Baselines

```python
import dataset_hub

housing = dataset_hub.regression.get_housing() # pd.DataFrame
```

## Installation
```bash
# Python 3.9+
pip install dataset-hub
```
If you run into installation issues, please write [here](https://github.com/GetDataset/dataset-hub/discussions/64)  

## Key Features

- **Unified one-line API** — load any dataset with `get_<dataset>()`.
- **Wide task coverage** — classification, regression, time series, and potentially more.
- **Rich documentation** — metadata, columns, examples, and source links.
- **Starter baselines** — quick starter models for every dataset.
- **Curated, not crowded** — a focused hub of easy-to-use, well-documented datasets.

## Supported Datasets

Every dataset in DatasetHub comes with a **ready-to-run baseline**, so you can start experimenting immediately.  

| Task           | Dataset | Quick Start |
|----------------|---------|-------------|
| Classification | [Titanic](https://getdataset.github.io/dataset-hub/datasets/classification/titanic.html) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GetDataset/dataset-hub/blob/main/notebooks/classification/titanic.ipynb) |
| Classification | [Iris](https://getdataset.github.io/dataset-hub/datasets/classification/iris.html) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GetDataset/dataset-hub/blob/main/notebooks/classification/iris.ipynb) |
| Regression     | [California Housing Prices](https://getdataset.github.io/dataset-hub/datasets/regression/california_housing.html) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GetDataset/dataset-hub/blob/main/notebooks/regression/california_housing.ipynb) |
| Time Series    | [Household Electric Power Consumption](https://getdataset.github.io/dataset-hub/datasets/timeseries/household_power.html) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GetDataset/dataset-hub/blob/main/notebooks/timeseries/household_power.ipynb) |





### 💡 **Have ideas for new datasets or features?**  
Join the [discussion](https://github.com/GetDataset/dataset-hub/discussions/63) and tell us what you'd like to see next.

## Why this library exists

Every time I wanted to try a new ML task from scratch, I faced a chain of steps:  
search for a suitable dataset → download it → load it into Python → write a baseline.  

Some of these steps were surprisingly complex, and sometimes I just gave up.  
The challenge grew even bigger when exploring new ML domains — take graph ML, for example — and honestly, I had no idea where to begin.

I created DatasetHub to solve this problem: it gives a **unified, easy-to-use interface** to access datasets, each with a ready-to-run baseline so you can start experimenting immediately.

## API Disclaimer

DatasetHub downloads datasets from external public sources. Because of this:

1. **Sources may become unavailable**  
If a dataset's original source (and mirrors) goes offline or changes, the corresponding `get_<dataset>()` function may stop working.
If this happens, please write [here](https://github.com/GetDataset/dataset-hub/discussions/64) 

2. **API may change**  
If a dataset is no longer publicly accessible, it may be removed from the library.

3. **Copyright**  
If a copyright holder requests removal of their dataset, we will comply and update the API accordingly.

## For copyright holders

If you believe your dataset should not be included, please contact us.
We will review the request and remove or restrict access promptly.

## Contributing

We’d love to have you on board!  
If you’re excited to help develop and grow DatasetHub, please let us know in the [discussion](https://github.com/GetDataset/dataset-hub/discussions/64).  
Once you express interest, we can provide guidance, suggest tasks, and outline contribution guidelines to help you get started.