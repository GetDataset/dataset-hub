import logging
from functools import wraps
from logging import Logger
from typing import Optional

from dataset_hub._core.settings.loader import load_settings


def get_logger(name: Optional[str] = None) -> Logger:
    """
    Get a configured logger instance for this library.

    This function returns a `logging.Logger` instance with a simple console
    StreamHandler attached. The logger is configured to:
        - Output messages at the INFO level.
        - Use a clean formatter: only the message text.
        - Prevent propagation to the root logger to avoid duplicate messages.

    Args:
        name (Optional[str]): The name of the logger. If None, the root logger is used.

    Returns:
        Logger: A `logging.Logger` instance ready to use.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logging.getLogger(name)


def log_dataset_doc_doc_link():
    """
    Decorator used by :ref:`get_data` to log a link to the dataset documentation.

    The purpose of this decorator is to keep the `get_data` function clean by
    separating the documentation logging logic. After `get_data` executes, this
    decorator will log a link to the dataset documentation if `verbose` is enabled
    (either passed as an argument or taken from global settings).

    Returns:
        Callable: The same `get_data` function, with documentation logging applied.

    Notes:
        - Logging is performed via the library's internal logger.
        - The decorator does **not** alter the return value of `get_data`.
        - Logging occurs **after** the function has executed.
        - If `verbose` is False, no message is logged.
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            from inspect import signature  # get arg values

            sig = signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            dataset_name = bound.arguments["dataset_name"]
            task_type = bound.arguments["task_type"]
            verbose = bound.arguments["verbose"]

            result = func(*args, **kwargs)

            if verbose is None:
                settings = load_settings()
                verbose = settings["verbose"]
            if verbose:
                # Build logger name to match the module where get_data is actually
                # called via the decorator in public dataset getters
                # (e.g. dataset_hub.classification.get_iris()). This ensures logs
                # appear in the correct namespace and are consistent with library
                # structure.
                logger_name = f"dataset_hub.{task_type}.datasets"
                logger = get_logger(logger_name)
                logger.info(
                    f'Dataset info & details: https://getdataset.github.io/dataset-hub/datasets/{task_type}/{dataset_name}.html'
                )

            return result

        return wrapper

    return decorator
