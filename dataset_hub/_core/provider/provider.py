from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ProviderConfig:
    """
    Abstract base class for all provider configurations.

    Concrete provider configs should inherit from this class.
    """

    pass


class Provider(ABC):
    """
    Abstract base class for all data providers.

    Each provider is responsible for loading a dataset from its source, which can
    be a URL, a local file, a sklearn dataset, or any other supported source.

    Attributes:
        config (Dict[str, Any]): The provider's configuration loaded from the dataset YAML file.
    """

    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Initialize the provider with the given configuration.

        Args:
            config (Dict[str, Any]): The raw configuration dictionary for the provider.

        The configuration is validated and/or normalized by the `_prepare_config` method
        and stored in `self.config`.
        """
        self.config: Dict[str, Any] = self._prepare_config(config)

    @abstractmethod
    def load(self) -> Dict[str, Any]:
        """
        Load and return the dataset according to the provider's configuration.

        Returns:
            Dict[str, Any]: The loaded dataset object.
        """
        ...

    @abstractmethod
    def _prepare_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and/or process the raw configuration dictionary
        .

        Args:
            cfg (Dict[str, Any]): The raw configuration dictionary.

        Returns:
            Dict[str, Any]: The validated and/or normalized configuration to be used
            by the provider.
        """
        ...
