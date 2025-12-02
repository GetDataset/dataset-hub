.. _quick_start:

**********
Quick Start
**********


This section shows how to load your first dataset using the unified
``get_<dataset>()`` API.

Basic example
-------------

Load any dataset in a familiar format (e.g., a pandas DataFrame) with a single function call:

.. code-block:: python

    import dataset_hub

    dataset = dataset_hub.classification.get_titanic()
    # Dataset info & details: https://getdataset.github.io/dataset-hub/datasets/classification/titanic.html
    
After calling the function, a link to the dataset page will appear in the log output.
It contains detailed information about the dataset (description, columns, target, etc.).

Next steps
----------

You can proceed in two ways:

    - Start your own experiments with the dataset (split into train and test, build validation, perform feature engineering, build models, etc.)
    - Use a ready-made baseline provided in the documentation 

For example, here is a simple baseline for :ref:`titanic`:

.. code-block:: python

    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score

    # Separate target variable (y) and features (X)
    y = dataset["survived"]
    X = dataset.drop("survived", axis=1)

    # Drop categorical columns for simplicity (you can preprocess them yourself)
    X = X.select_dtypes(include=["int64", "float64"])

    # Fill missing numeric values
    for col in X.columns:
        X[col] = X[col].fillna(X[col].median())

    # Split data into train and test parts
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Create and train the model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", round(accuracy, 3))  # Example output: 0.706

Available datasets
------------------

See the full list here: :ref:`datasets`

Or jump directly to the quick examples:

- :ref:`titanic`
- :ref:`iris`
- :ref:`california_housing`

