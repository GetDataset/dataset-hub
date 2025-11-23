from typing import Dict, Any

def transform_config(config: Dict[str, Any]) -> Dict[str, Any]:
    config["source_transform"] = config.get("source_transform", [])
    return config