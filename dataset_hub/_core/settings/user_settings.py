from typing import Any

RUNTIME_SETTINGS = {}


def set_option(
    key: str, value: Any
) -> None:  # TODO add validating keys and values and rise Errors
    """Set a DatasetHub configuration option.

    Updates a runtime setting that affects DatasetHub behavior for the
    current Python session.

    Args:
        key (str): Name of the option to set.
        value (Any): New value assigned to the option.

    Example:

        .. code-block:: python

            import dataset_hub

            dataset_hub.set_option("verbose", False)
    """
    RUNTIME_SETTINGS[key] = value
