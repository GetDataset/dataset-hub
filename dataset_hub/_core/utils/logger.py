import logging
from logging import Logger
from typing import Optional

def get_logger(name: Optional[str] = None) -> Logger:
    """
    Возвращает логгер для внутреннего использования.
    """
    return logging.getLogger(name)