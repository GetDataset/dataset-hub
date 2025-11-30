from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, Generic, Type

Buffer = None

class SourceLoader(ABC):


    def __init__(self, config: Dict[str, Any]) -> None:
        pass

    def load(self) -> Dict[str, None]:
        pass