from typing import Dict, Any
from dataset_hub._core.provider import ProviderFactory
from dataset_hub._core.utils.config import ConfigFactory


def get_data(dataset_name: str, task_type: str) -> Dict[str, Any]:
    """
    Core for main public API function

    Параметры:
        dataset_name: str — название датасета
        task_type: str — опционально, тип задачи

    Возвращает:
        dict {table_name: pd.DataFrame}
    """
    config = ConfigFactory.load_config(dataset_name, task_type)
    provider = ProviderFactory.build_provider(config["provider"])
    dataset = provider.load()

    return dataset