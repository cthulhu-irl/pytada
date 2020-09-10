from abc import ABC, abstractmethod


class JSONConvertable(ABC):

    @abstractmethod
    def to_json(obj):
        """ convert the given obj to json string """
        pass

    @abstractmethod
    def from_json(cls, string):
        """
        converts the given json string to an instance of this class
        """
        pass
