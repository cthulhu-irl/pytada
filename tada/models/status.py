from abc import ABC, abstractmethod

from .base import Model
from ..query.base import Comparable

class StatusBase(ABC, Comparable, Model):

    @abstractmethod
    def __str__(self):
        pass

class Status(StatusBase):

    def __init__(self, string):
        pass

    def __str__(self):
        pass

    def __cmp__(self, other):
        pass

    def to_raw(obj):
        pass

    @classmethod
    def from_raw(cls, string):
        pass

