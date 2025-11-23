from typing import Dict, Any
from dataset_hub._core.registry.load import load_config
from dataset_hub._core.registry.transform import transform_config
from dataset_hub._core.sources.transform import transform_raw
from dataset_hub._core.sources.download import download_raw
from dataset_hub._core.tables.load import load_table
from dataset_hub._core.tables.transform import transform_table
from dataset_hub._core.common.logger import get_logger

logger = get_logger(__name__)

def get_data(dataset_name: str = 'titanic', task_type: str = 'classification') -> Dict[str, Any]:
    """
    Публичный API: возвращает словарь {table_name: DataFrame}.
    
    Параметры:
        dataset_name: str — название датасета
        task_type: str — опционально, тип задачи
    
    Возвращает:
        dict {table_name: pd.DataFrame}
    """
    config = get_config(dataset_name, task_type)

    get_source(config)

    tables = {}
    for table_config in config['tables']:
        tables[table_config["name"]] = get_table(table_config)

    return tables


def get_source(config: Dict[str, Any]):
    for source_config in config["sources"]:
        download_raw(source_config)
    
    for transform_config in config["source_transform"]:
        transform_raw(transform_config)


def get_table(table_config: Dict[str, Any]):
    table = load_table(table_config["file"], table_config["read_params"])
    table = transform_table(table)

    return table

def get_config(dataset_name: str, task_type: str) -> Dict[str, Any]:
    config = load_config(dataset_name, task_type)
    config = transform_config(config)
    
    return config