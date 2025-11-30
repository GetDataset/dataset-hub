from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, Generic, Type, TypeVar


BufferPackT = TypeVar("BufferPackT")


class BufferPackager(ABC, Generic[BufferPackT]):


    def __init__(self, config: Dict[str, Any]) -> None:
        pass

    def pack(self) -> Dict[str, None]: #TODO rename this
        pass