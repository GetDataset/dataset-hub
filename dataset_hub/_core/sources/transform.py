from pathlib import Path
from .download import _download_raw

# --- простые трансформации ---
def unzip(params):
    import zipfile
    target_dir = Path(params["target_dir"])
    zip_file = params["file"]
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(target_dir)

def move(params):
    import shutil
    import glob
    files = glob.glob(params["from"])
    target_dir = Path(params["to"])
    target_dir.mkdir(parents=True, exist_ok=True)
    for f in files:
        shutil.move(f, target_dir / Path(f).name)

# --- registry ---
TRANSFORM_REGISTRY = {
    "unzip": unzip,
    "move": move,
}

def transform_raw(local_files, transform_list):
    """
    Применяет трансформации к скачанным файлам.
    """
    for action in transform_list:
        transform_name = action["transform"]
        params = action.get("params", {})
        # Если нужно передать путь к файлу в unzip/move
        if "file" in params and params["file"] == "__auto__":
            params["file"] = local_files[0]  # пример, можно улучшить для нескольких файлов
        if transform_name not in TRANSFORM_REGISTRY:
            raise ValueError(f"Unknown transform {transform_name}")
        TRANSFORM_REGISTRY[transform_name](params)