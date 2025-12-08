[![PyPI version](https://img.shields.io/pypi/v/dataset-hub.svg)](https://pypi.org/project/dataset-hub/0.1.0/)
[![Datasets docs](https://img.shields.io/badge/docs-dataset?label=dataset-hub)](https://getdataset.github.io/dataset-hub/index.html)

# DatasetHub: A Unified API for Exploring Any ML Task

```python
import dataset_hub

housing = dataset_hub.regression.get_housing() # pd.DataFrame
# Dataset info & details: https://getdataset.github.io/dataset-hub/datasets/classification/titanic.html
```

## Installation
```bash
# Python 3.9+
pip install dataset-hub
```
If you encounter any installation issues (OS-specific or otherwise), please check or post in the existing discussion:
[Bug Reports, Installation Issues & Q&A](https://github.com/GetDataset/dataset-hub/discussions/64)  

## Key Features

- **Unified one-line API** — load any dataset with `.get_<dataset>()`.
- **Wide task coverage** — classification, regression, time series, and potentially more.
- **Rich documentation** — metadata, columns, examples, and source links.
- **Starter baselines** — quick starter models for every dataset.
- **Curated, not crowded** — a focused hub of easy-to-use, well-documented datasets.


## Supported Datasets

Each dataset includes a detailed documentation page with metadata, columns, sources, and a prepared baseline.

### Classification
- **Titanic**  
  [Documentation](https://getdataset.github.io/dataset-hub/datasets/classification/titanic.html)
- **Iris**  
  [Documentation](https://getdataset.github.io/dataset-hub/datasets/classification/iris.html)

### Regression
- **California Housing Prices**  
  [Documentation](https://getdataset.github.io/dataset-hub/datasets/regression/california_housing.html)

### Time Series
- **Household Electric Power Consumption**  
  [Documentation](https://getdataset.github.io/dataset-hub/datasets/timeseries/household_power.html)


## Why this library exists
DatasetHub was created to provide a single, unified entry point for experimenting with any classic ML task — from scoring and forecasting to fraud detection and uplift modeling.

Looking ahead, the project focuses on two major directions:

1. **Assemble a large collection of open datasets** for a variety of classic ML tasks, all easily accessible through the unified `.get_<dataset>()` interface.

2. **Provide realistic, ready-to-use synthetic datasets** that mimic real-world business scenarios, enabling experimentation for niche tasks where open data is scarce.

## API Disclaimer

1. **Temporary issues**  
Our dataset functions rely on external sources. If a source and mirror sources become unavailable or temporarily fail, a function may stop working temporarily or completely.  
If you encounter a persistent issue under such circumstances, please open an issue and provide detailed information about your attempts.

2. **Dynamic API**  
If all available sources and mirror sources for a dataset completely disappear and the dataset is no longer publicly accessible, our API may change, and the dataset may be removed. Please be prepared for this possibility.

3. **Copyright concerns**  
Similar changes may occur if a copyright holder requests the removal of access to a dataset.

## For copyright holders

If you believe your data should not be included or accessible via this project, please contact us directly. We will promptly review your request and take appropriate action to remove or restrict access to the dataset in question.

## Contributing

Currently there is no formal contribution guide.  
If you'd like to contribute a new dataset, report a bug, or suggest an improvement, please start a discussion here:  
[Bug Reports, Installation Issues & Q&A](https://github.com/GetDataset/dataset-hub/discussions/64)  

We welcome community contributions and will provide guidance in the discussion thread.