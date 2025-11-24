from pathlib import Path

from dataset_hub._settings.loader import load_settings


def build_datafile_path(dataset_name: str, filename: str) -> Path:
    """
    Construct the full path to a dataset file and create necessary directories.

    Args:
        dataset_name (str): The name of the dataset (e.g., 'titanic').
        filename (str): The name of the file. Must be provided.

    Returns:
        Path: The full path to the dataset file.
    """
    settings = load_settings()
    data_path = settings["data_path"]

    path = Path(data_path) / dataset_name
    path.mkdir(parents=True, exist_ok=True)

    return path / filename


def list_available_datasets(task_type: str) -> list[str]:
    """
    List all available dataset names for a given task type.

    Args:
        task_type (str): The type of task (used to locate the exists configs).

    Returns:
        List[str]: A list of dataset names (without file extensions).
    """
    task_configs_path = Path(__file__).parent.parent.parent / task_type / "_configs"
    return [p.stem for p in task_configs_path.glob("*.yaml")]
