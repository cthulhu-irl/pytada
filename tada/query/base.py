from abc import ABC, abstractmethod

class Comparable(ABC):

    @abstractmethod
    def __cmp__(self, other):
        pass

