from abc import ABC, abstractmethod


class RAWConvertable(ABC):

    @abstractmethod
    def to_raw(obj):
        """
        converts the given obj to pure primary types instances
        """
        pass

    @abstractmethod
    def from_raw(cls, raw):
        """
        converts the given raw of pure primary types to
        an instance of this class
        """
        pass
