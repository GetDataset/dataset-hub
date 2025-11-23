import pandas as pd

def load_table(file_path, read_params=None):
    read_params = read_params or {}
    return pd.read_csv(file_path, **read_params)