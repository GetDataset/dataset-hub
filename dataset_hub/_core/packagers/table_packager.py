from .buffer_packager import BufferPackager
from typing import Optional, Dict

class TableBufferPack:
    
    def __init__(self, data: bytes):
        self.data = data

class TableBufferPackager(BufferPackager[TableBufferPack]):

    def package(self, buffers: Dict[str, bytes]) -> TableBufferPack:
        return TableBufferPack(
            data=buffers.get("data"),
        )