import pandas as pd
from typing import Dict, Any

def load_tables(config: Dict[str, Any]) -> Dict[str, Any]:
    tables = {}
    for table_config in config['tables']:
        table = load_table(table_config["file"], table_config["read_params"])
        tables[table_config["name"]] = table
    return tables

def load_table(file_path, read_params=None):
    read_params = read_params or {}
    return pd.read_csv(file_path, **read_params)