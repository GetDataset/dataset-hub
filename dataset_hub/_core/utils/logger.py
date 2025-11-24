import logging
from logging import Logger
from typing import Optional


def get_logger(name: Optional[str] = None) -> Logger:
    """
    Get a logger instance with the specified name.

    Args:
        name (Optional[str]): The name of the logger. If None, the root logger is returned.

    Returns:
        Logger: A logging.Logger instance corresponding to the given name.
    """
    return logging.getLogger(name)
