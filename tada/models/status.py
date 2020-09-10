from abc import ABC, abstractmethod

from .base import Model
from ..query.base import Comparable


class StatusBase(ABC, Comparable, Model):
    """ abstract comparable status model class """

    @abstractmethod
    def __str__(self):
        pass


class Status(StatusBase):
    """
    status model with 3 states of todo, doing and done
    with string representation of -, x and +
    respectively
    """

    TODO = 0
    DOING = 1
    DONE = 2
    STRINGS = ['-', 'x', '+']

    def __init__(self, stat):
        if isinstance(stat, str) and stat in self.STRINGS:
            self.string = stat
            self.index = self.STRINGS.index(stat)

        strs_len = len(self.STRINGS)
        if isinstance(stat, int) and 0 <= stat < strs_len:
            self.string = self.STRINGS[stat]
            self.index = stat

        raise ValueError(
            'given `stat` is not an Status representative'
        )

    def __str__(self):
        return self.string

    def __cmp__(self, other):
        return self.index.__cmp__(other.index)

    def to_raw(obj):
        return str(obj)

    @classmethod
    def from_raw(cls, string):
        return cls(string)
