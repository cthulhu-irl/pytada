from abc import ABC, abstractmethod

from ..utils.general import and_fn, or_fn, xor_fn

class Comparable(ABC):

    @abstractmethod
    def __cmp__(self, other):
        pass

class LogicallyComposible(object):

    def __and__(self, fn):
        return self.and_(fn)

    def __or__(self, fn):
        return self.or_(fn)

    def __xor__(self, fn):
        return self.xor_(fn)

    def and_(self, fn):
        return self.map(lambda f: and_fn(f, fn))

    def or_(self, fn):
        return self.map(lambda f: or_fn(f, fn))

    def xor_(self, fn):
        return self.map(lambda f: xor_fn(f, fn))

