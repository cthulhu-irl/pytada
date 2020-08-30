from abc import ABC, abstractmethod

class RAWConvertible(ABC):

    @abstractmethod
    def to_raw(obj):
        pass

    @abstractmethod
    def from_raw(cls, string):
        pass

