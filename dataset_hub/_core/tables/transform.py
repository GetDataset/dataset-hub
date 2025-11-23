from typing import Dict, Any
from dataset_hub._core.tables.dataset import Dataset

def transform_tables(tables: Dataset) -> Dataset:
    for table_name, table in tables.items():
        tables[table_name] = transform_table(table)
    return tables

def transform_table(table: Any) -> Any:
    return table