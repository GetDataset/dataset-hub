from typing import Type, Dict, Any
from .provider import Provider
from .url_provider import UrlProvider


class ProviderFactory:
    """
    Factory to build Provider instances based on a configuration dictionary.

    Uses a simple strategy pattern: selects the provider class by 'type' key in config.
    """

    # Registry mapping type string -> Provider class
    _registry: Dict[str, Type[Provider]] = {
        "url": UrlProvider
    }

    @classmethod
    def build_provider(cls, provider_config: Dict[str, Any]) -> Provider:
        """
        Build a Provider instance from a configuration dictionary.

        Args:
            provider_config (Dict[str, Any]): The configuration dict with at least a 'type' and 'params' keys.

        Returns:
            Provider: An instance of the appropriate Provider subclass.

        Raises:
            ValueError: If the type is not registered.
        """
        provider_type = provider_config.get("type")
        if not provider_type:
            raise ValueError("Provider config must include a 'type' key")

        provider_params = provider_config.get("params")
        if not provider_params:
            raise ValueError("Provider config must include a 'params' key")

        provider_cls = cls._registry.get(provider_type)
        if not provider_cls:
            raise ValueError(f"No provider registered for type '{provider_type}'")

        return provider_cls(provider_params)
