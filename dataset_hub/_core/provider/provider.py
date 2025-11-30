from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, Generic, Type

from dataset_hub._core.data_bundle import UserDataT


@dataclass
class ProviderConfig:
    """
    Base class for all provider configuration models.

    Concrete provider configurations must inherit from this class.
    These dataclasses define the structure, defaults, and type hints
    for a provider's configuration, and are used by the Provider class
    to validate and normalize incoming config dictionaries.
    """

    pass


class Provider(ABC, Generic[UserDataT]):
    """
    Abstract base class for all data providers.

    A provider loads a dataset from some source (URL, file, built-in dataset, etc.)
    according to a configuration model defined in `ConfigClass`.

    The provider lifecycle consists of:
        1. Normalization — convert a raw dict into a validated config dict
           using the dataclass `ConfigClass`.
        2. Optional transformation — post-process or enrich the normalized config.
        3. Data loading — implemented in `load()`.

    Attributes:
        config (Dict[str, Any]):
            The validated and optionally transformed configuration dictionary.
        ConfigClass (Type[ProviderConfig]):
            A dataclass defining the structure of the provider's configuration.
            Must be overridden by subclasses.
    """

    ConfigClass: Type[ProviderConfig]

    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Initialize the provider with the given raw configuration dictionary.

        The initialization pipeline consists of two stages:
            - `_normalize_config()`: Validate and normalize the raw config using
            the provider's `ConfigClass` dataclass.
            - `_transform_config()`: Optionally apply additional processing to the
            normalized configuration.

        The final result of both steps is stored in `self.config`.

        Args:
            config (Dict[str, Any]):
                The raw configuration dictionary supplied by the dataset definition.

        Raises:
            TypeError:
                If the subclass does not define a valid `ConfigClass`.
            ValueError:
                If the configuration cannot be validated against `ConfigClass`.
        """

        if self.ConfigClass is None:
            raise TypeError(
                f"{self.__class__.__name__} must define ConfigClass = SomeDataclass"
            )
        normalized = self._normalize_config(config)
        transformed = self._transform_config(normalized)
        self.config = transformed

    @abstractmethod
    def load(self) -> UserDataT:
        """
        Load and return the dataset according to the provider's configuration.

        This method must be implemented by all concrete providers.

        Returns:
            Any: The loaded dataset object. Typically a pd.DataFrame for single-table
            datasets, but can be any data type (e.g., dict, list, graph, array).
        """
        ...

    def _normalize_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate and normalize the raw configuration using the provider's ConfigClass.

        This method constructs an instance of `ConfigClass` from the raw dictionary.
        This enforces field types, required fields, and applies default values defined
        in the dataclass. The resulting dataclass instance is then converted back into
        a plain dictionary.

        Subclasses normally do not override this method.

        Args:
            config (Dict[str, Any]):
                The raw configuration dictionary.

        Returns:
            Dict[str, Any]:
                A normalized configuration dictionary.

        Raises:
            ValueError:
                If the config does not match the dataclass signature.
        """
        try:
            inst = self.ConfigClass(**config)
        except TypeError as e:
            raise ValueError(
                f"Invalid config for {self.__class__.__name__}: {e}"
            ) from e

        return asdict(inst)

    def _transform_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply optional post-processing to the normalized configuration.

        This hook allows subclasses to perform additional adjustments to the
        configuration after dataclass validation.

        By default, this method returns the configuration unchanged.

        Args:
            config (Dict[str, Any]):
                The already normalized configuration dictionary.

        Returns:
            Dict[str, Any]:
                The transformed configuration dictionary.
        """
        return config
