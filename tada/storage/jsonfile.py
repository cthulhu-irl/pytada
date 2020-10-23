from typing import Any, Type

from .base import TokenBase, StorageManagerBase


class JSONFileStorage(StorageManagerBase):

    def __init__(self, filename: str) -> None:
        pass

    def query(self, token: TokenBase) -> 'JSONFileStorage':
        pass

    def loadout(self) -> Any:
        pass

    def persist(self) -> 'JSONFileStorage':
        pass
