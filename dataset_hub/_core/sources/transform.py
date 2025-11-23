from dataset_hub._core.registry.config import Config

# --- registry ---
TRANSFORM_REGISTRY = {
}

def transform_raw(config: Config) -> None:
    for transform_config in config["source_transform"]:

        transform_type = transform_config["transform_type"]
        if transform_type not in TRANSFORM_REGISTRY:
            raise ValueError(f"Unknown transform type {transform_type}")
        transform_func = TRANSFORM_REGISTRY[transform_type]
        transform_func(**transform_config["transform_params"])