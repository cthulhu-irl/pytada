from abc import ABC, abstractmethod

from .base import Model
from ..serializers.base import SerializerBase

class StatusBase(ABC, SerializerBase):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __cmp__(self, other):
        pass

class Status(StatusBase, Model):

    def __init__(self, string):
        pass

    def __str__(self):
        pass

    def __cmp__(self, other):
        pass

    @classmethod
    def serialize(cls, obj):
        pass

    @classmethod
    def deserialize(cls, string):
        pass

