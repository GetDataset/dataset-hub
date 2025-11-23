from pathlib import Path
from dataset_hub._core.sources.download_utils import url2file
from dataset_hub._core.utils.paths import build_datafile_path
from dataset_hub._core.registry.config import Config


# --- main download interface ---
def download_raw(config: Config) -> None:
    """
    Load files from sources using registry
    """
    for source_config in config["sources"]:
        source_path = build_datafile_path(
            dataset_name=config["dataset_name"],
            filename=source_config["file"]
        )

        if source_path.exists():
            continue  # skip existing files
        
        source_type = source_config["source_type"]
        if source_type not in DOWNLOAD_REGISTRY:
            raise ValueError(f"Unknown source type {source_type}")
        
        download_source = DOWNLOAD_REGISTRY[source_type]
        download_source(source_config, source_path)

# --- "url" source type ---
def download_url(source_config: Config, save_path: Path) -> None:
    """
    Load source using HTTP/HTTPS URL.
    """
    url = source_config["source_info"]["url"]
    url2file(url, save_path)

# --- registry of download types ---
DOWNLOAD_REGISTRY = {
    "url": download_url
}

