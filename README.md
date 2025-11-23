# DatasetHub: A Unified API for Exploring Any ML Task


**DatasetHub** is an educational project that provides a simple `dataset_hub.<task>.get_data()` API to access datasets.
```python
import dataset_hub

dataset = dataset_hub.classification.get_data('titanic')
titanic = dataset['titanic']
print(type(titanic)) # pandas.DataFrame
```
It lets beginners access datasets effortlessly, while giving practitioners a single interface to experiment with any open dataset or ML task.

## Quickstart for Any Task
```python
import dataset_hub
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

dataset = dataset_hub.uplift.get_data('hillstrom')
data = dataset["data"]
target = dataset["target"]
treatment = dataset["treatment"]

X_train, X_test, y_train, y_test, tr_train, tr_test = train_test_split(
    data, target, treatment, test_size=0.2, random_state=42, maintain_proportions=True
)

model = RandomForestClassifier()
model.fit(X_train[tr_train==0], y_train[tr_train==0]) # tr_train==0 filters control group for model fitting
preds = model.predict(X_test)
```

You can take any task from DatasetHub and start exploring or modeling immediately, whether it’s classification, regression, or uplift modeling.

## Installation
```bash
# Python 3.8+
pip install dataset_hub
```

## Available tasks and datasets:
dataset-hub.docs.com

## Why this library exists
DatasetHub was created to provide a single, unified entry point for experimenting with any classic ML task — from classification, scoring, and forecasting to pricing, fraud detection, and uplift modeling.

Looking ahead, the project focuses on two major directions:

1. **Assemble a large collection of open datasets** for a variety of classic ML tasks, all easily accessible through the unified `dataset_hub.<task>.get_data()` interface.

2. **Provide realistic, ready-to-use synthetic datasets** that mimic real-world business scenarios, enabling experimentation for niche tasks where open data is scarce.

