import yaml
from pathlib import Path
from dataset_hub._core.utils.logger import get_logger
from dataset_hub._core.registry.config import Config

logger = get_logger(__name__)

def load_config(dataset_name: str, task_type: str) -> Config:
    """
    Загружает конфиг датасета по имени.
    
    Параметры:
        dataset_name: str — название датасета (имя файла без расширения)
    
    Возвращает:
        dict — содержимое YAML конфига
    """
    config_path = build_config_path(dataset_name, task_type)
    config = load_raw_config(config_path)
    config = normalize_config(config)
    
    return config

def build_config_path(dataset_name: str, task_type: str) -> Path:
    current_file_path = Path(__file__).resolve()
    dataset_hub_path = current_file_path.parent.parent.parent
    config_path = dataset_hub_path / task_type / "_configs" / f"{dataset_name}.yaml"
    return config_path

def load_raw_config(config_path: Path) -> Config:
    if not config_path.exists():
        raise FileNotFoundError(f"Dataset config not found: {config_path.parts[-3:]}")

    with open(config_path) as f:
        dataset_cfg = yaml.safe_load(f)

    return dataset_cfg

def normalize_config(config: Config) -> Config:
    if config.get("source_transform", None) is None: 
        config["source_transform"] = []
    for table in config["tables"]:
        if "read_params" not in table:
            table["read_params"] = {}
    return config