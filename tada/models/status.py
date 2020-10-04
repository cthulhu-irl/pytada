from abc import abstractmethod
from typing import ClassVar, Union, List

from pydantic import validator

from .base import Model
from ..query.base import Comparable

class Status(Model, Comparable):
    """
    status model with 3 states of todo, doing and done
    with string representation of -, x and +
    respectively
    """

    TODO: ClassVar[int] = 0
    DOING: ClassVar[int] = 1
    DONE: ClassVar[int] = 2
    STRINGS: ClassVar[List[str]] = ['-', 'x', '+']

    status: str

    def __init__(self, status: Union[str, int, 'Status']) -> None:
        return super(Status, self).__init__(status=status)

    @validator('status', pre=True)
    def different_status_type(cls, stat: Union[str, int, 'Status']) -> str:
        strs_len = len(cls.STRINGS)

        if isinstance(stat, str) and stat in cls.STRINGS:
            status = stat

        elif isinstance(stat, int) and 0 <= stat < strs_len:
            status = cls.STRINGS[stat]

        elif isinstance(stat, Status):
            status = stat.status

        else:
            raise ValueError(
                'given `stat` is not an Status representative'
            )

        return status

    def __str__(self) -> str:
        return self.status

    def __cmp__(self, other: 'Status') -> int:
        return self.index - other.index

    @property
    def index(self) -> int:
        return self.STRINGS.index(self.status)

    def to_raw(obj: 'Status') -> str:
        return str(obj)

    @classmethod
    def from_raw(cls, string: str) -> 'Status':
        return cls(status=string)
