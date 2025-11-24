from typing import Dict, Any
from pathlib import Path
import yaml

class ConfigFactory:
    """
    Factory to load and build dataset configurations.

    Responsibilities:
        - Find config file by dataset_name and task_type
        - Load YAML into dict
    """

    @staticmethod
    def load_config(dataset_name: str, task_type: str) -> Dict[str, Any]:
        """
        Load and return the dataset configuration as a dictionary.

        Args:
            dataset_name (str): Name of the dataset (file without extension).
            task_type (str): Type of task (e.g., "classification").

        Returns:
            dict: Loaded configuration from the YAML file.
        """
        config_path = ConfigFactory.build_config_path(dataset_name, task_type)
        config = ConfigFactory.load_raw_config(config_path)
        return config

    @staticmethod
    def build_config_path(dataset_name: str, task_type: str) -> Path:
        """
        Build the file path to the dataset's YAML configuration.

        Args:
            dataset_name (str): Name of the dataset.
            task_type (str): Type of task.

        Returns:
            Path: Full path to the YAML config file.
        """
        current_file_path = Path(__file__).resolve()
        dataset_hub_path = current_file_path.parent.parent.parent
        config_path = dataset_hub_path / task_type / "_configs" / f"{dataset_name}.yaml"
        return config_path

    @staticmethod
    def load_raw_config(config_path: Path) -> Dict[str, Any]:
        """
        Load the raw YAML configuration from the given path.

        Args:
            config_path (Path): Path to the YAML configuration file.

        Returns:
            dict: Configuration loaded from YAML.

        Raises:
            FileNotFoundError: If the YAML file does not exist.
        """
        if not config_path.exists():
            raise FileNotFoundError(f"Dataset config not found: {config_path.parts[-3:]}")
        with open(config_path) as f:
            dataset_config = yaml.safe_load(f)
        return dataset_config