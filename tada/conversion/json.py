from abc import ABC, abstractmethod

class JSONConvertable(ABC):

    @abstractmethod
    def to_json(obj):
        pass

    @abstractmethod
    def from_json(cls, string):
        pass

