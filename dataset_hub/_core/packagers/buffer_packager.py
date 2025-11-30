from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, Generic, Type, TypeVar


BufferPackT = TypeVar("BufferPackT")


class BufferPackager(ABC, Generic[BufferPackT]):

    @abstractmethod
    def package(self, buffers: Dict[str, bytes]) -> BufferPackT:
        pass