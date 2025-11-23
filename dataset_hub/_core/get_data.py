from typing import Dict, Any
from dataset_hub._core.registry.load import load_config
from dataset_hub._core.registry.transform import transform_config
from dataset_hub._core.sources.transform import transform_raw
from dataset_hub._core.sources.download import download_raw
from dataset_hub._core.tables.load import load_tables
from dataset_hub._core.tables.transform import transform_tables
from dataset_hub._core.utils.logger import get_logger

logger = get_logger(__name__)

def get_data(dataset_name: str, task_type: str) -> Dict[str, Any]:
    """
    Core for main public API function
    
    Параметры:
        dataset_name: str — название датасета
        task_type: str — опционально, тип задачи
    
    Возвращает:
        dict {table_name: pd.DataFrame}
    """
    config = get_config(dataset_name, task_type)
    get_source(config)
    tables = get_tables(config)

    return tables

def get_config(dataset_name: str, task_type: str) -> Dict[str, Any]:
    config = load_config(dataset_name, task_type)
    config = transform_config(config)
    
    return config

def get_source(config: Dict[str, Any]):
    download_raw(config)
    
    for transform_config in config["source_transform"]:
        transform_raw(transform_config)

def get_tables(config: Dict[str, Any]) -> Dict[str, Any]:
    tables = {}
    tables = load_tables(config)
    tables = transform_tables(tables)

    return tables