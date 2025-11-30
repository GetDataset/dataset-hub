from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, Generic, Type
from dataset_hub._core.packagers.buffer_packager import BufferPackT
from dataset_hub._core.data_bundle import UserDataT

class BufferParser(ABC, Generic[BufferPackT, UserDataT]):


    def __init__(self, config: Dict[str, Any]) -> None:
        pass

    def parse(self) -> Dict[str, None]: #TODO rename this
        pass