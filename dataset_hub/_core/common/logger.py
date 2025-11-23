import logging


def get_logger(name: str | None = None):
    """
    Возвращает логгер для внутреннего использования.
    """
    return logging.getLogger(name)