import requests
from pathlib import Path

def download_raw(source_cfg):
    """
    Скачивает файл из основного источника или зеркала.
    Возвращает локальный путь к скачанному файлу.
    """
    url = source_cfg["source_info"]["url"]
    filename = Path(source_cfg["name"])
    
    if not filename.exists():
        resp = requests.get(url)
        resp.raise_for_status()
        filename.write_bytes(resp.content)
    return filename