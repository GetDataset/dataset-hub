import pandas as pd
from typing import Dict, Any
from pathlib import Path
from dataset_hub._core.utils.paths import build_datafile_path
from dataset_hub._core.registry.config import Config
from dataset_hub._core.tables.dataset import Dataset

def load_tables(config: Config) -> Dataset:
    tables = {}
    for table_config in config['tables']:
        table_path = build_datafile_path(
            dataset_name=config["dataset_name"],
            filename=table_config["file"]
        )
        table = load_table(table_path, table_config["read_params"])
        tables[table_config["name"]] = table
        
    return tables

def load_table(file_path: Path, read_params: Dict[str, Any]) -> Any:
    return pd.read_csv(file_path, **read_params)