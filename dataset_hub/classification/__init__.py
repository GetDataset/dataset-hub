from dataset_hub._core.get_data import get_data as _get_data

def get_data(dataset_name: str = 'titanic', **params):
    return _get_data(dataset_name, task_type="classification", **params)