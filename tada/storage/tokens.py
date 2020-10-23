from typing import ClassVar

from .base import TokenType, TokenBase

class Fx(TokenBase):
    _tokentype: ClassVar[TokenType] = TokenType.FX


class Create(TokenBase):
    _tokentype: ClassVar[TokenType] = TokenType.CREATE

class Retrieve(TokenBase):
    _tokentype: ClassVar[TokenType] = TokenType.RETRIEVE

class Update(TokenBase):
    _tokentype: ClassVar[TokenType] = TokenType.UPDATE

class Delete(TokenBase):
    _tokentype: ClassVar[TokenType] = TokenType.DELETE
