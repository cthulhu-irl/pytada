from enum import Enum
from abc import ABC, abstractmethod
from typing import Any, Type, ClassVar, TypeVar

from pydantic import BaseModel

SMT = TypeVar('SMT', bound='StorageManagerBase')

class TokenType(Enum):
    FX = 0

    CREATE = 1
    RETRIEVE = 2
    UPDATE = 3
    DELETE = 4

class TokenBase(ABC):

    def __call__(self, storage_manager: SMT) -> SMT:
        return self.q(storage_manager)

    @abstractmethod
    def tokentype(self) -> TokenType:
        pass

    def q(self, storage_manager: SMT) -> SMT:
        return storage_manager.query(self)

class TokenModel(TokenBase, BaseModel):
    _tokentype: ClassVar[TokenType]

    def tokentype(self) -> TokenType:
        return self._tokentype

class StorageManagerBase(ABC):

    @abstractmethod
    def query(self, token: TokenBase) -> SMT:
        pass

    @abstractmethod
    def loadout(self) -> Any:
        pass

    @abstractmethod
    def persist(self) -> SMT:
        pass
