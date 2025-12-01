from pathlib import Path
from typing import Any, Dict

import yaml


class ConfigManager:
    """
    Factory to load and build dataset configurations.

    Responsibilities:
        - Find config file by dataset_name and task_type
        - Load YAML into dict
        - Transform dataset_parts schema into provider-based schema
    """

    @staticmethod
    def load_config(dataset_name: str, task_type: str) -> Dict[str, Any]:
        """
        Load and return the dataset configuration as a dictionary.

        Converts from the dataset_parts schema to the provider-based schema:
            Input:  {"dataset_parts": [{"name": "...", "source": {...}, ...}]}
            Output: {"provider": {"type": "...", "params": {...}}}

        Args:
            dataset_name (str): Name of the dataset (file without extension).
            task_type (str): Type of task (e.g., "classification").

        Returns:
            dict: Loaded configuration with provider-based schema.
        """
        config_path = ConfigManager.build_config_path(dataset_name, task_type)
        raw_config = ConfigManager.load_raw_config(config_path)
        transformed_config = ConfigManager._transform_to_provider_schema(raw_config)
        return transformed_config

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
        dataset_hub_path = current_file_path.parent.parent
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
            raise FileNotFoundError(
                f"Dataset config not found: {config_path.parts[-3:]}"
            )
        with open(config_path) as f:
            dataset_config: Dict[str, Any] = yaml.safe_load(f)
        return dataset_config

    @staticmethod
    def _transform_to_provider_schema(raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform dataset_parts schema into provider-based schema.

        Input schema:
            dataset_parts:
              - name: "iris"
                pack_type: "table"
                as_type: "pd.DataFrame"
                source:
                  type: "url"
                  url: "https://..."
                  format: "csv"
                read_kwargs:
                  sep: ","

        Output schema:
            provider:
              type: "dataframe"
              params:
                source:
                  type: "url"
                  url: "https://..."
                  format: "csv"
                read_kwargs:
                  sep: ","

        Args:
            raw_config (Dict[str, Any]): Raw configuration with dataset_parts.

        Returns:
            Dict[str, Any]: Configuration with provider-based schema.

        Raises:
            ValueError: If the configuration structure is invalid.
        """
        if "dataset_parts" not in raw_config:
            raise ValueError("Configuration must contain 'dataset_parts' key")

        dataset_parts = raw_config["dataset_parts"]
        if not isinstance(dataset_parts, list) or len(dataset_parts) == 0:
            raise ValueError("'dataset_parts' must be a non-empty list")

        # Take the first dataset part (for now, support single-part datasets)
        part = dataset_parts[0]

        if "source" not in part:
            raise ValueError("Dataset part must contain 'source' key")

        source = part["source"]
        if "type" not in source:
            raise ValueError("Source must contain 'type' key")

        # Build provider params from source and read_kwargs
        params: Dict[str, Any] = {
            "source": source,
        }

        if "read_kwargs" in part:
            params["read_kwargs"] = part["read_kwargs"]

        # Return provider-based schema
        return {
            "provider": {
                "type": "dataframe",
                "params": params,
            }
        }
