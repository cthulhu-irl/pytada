from abc import ABC, abstractmethod

from ..utils.general import and_fn, or_fn


class Comparable(ABC):
    """ comparable mixin """

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    @abstractmethod
    def __cmp__(self, other):
        pass


class LogicallyComposable(object):
    """
    mixin class to make a function composer
    to be also logically composable through and_/or_ methods
    which give more readablitiy as they come like infix
    operators
    this class also aliases __and__/__or__ methods
    to and_/or_ methods
    """

    def __and__(self, fn):
        return self.and_(fn)

    def __or__(self, fn):
        return self.or_(fn)

    def and_(self, fn):
        return self.map(lambda f: and_fn(f, fn))

    def or_(self, fn):
        return self.map(lambda f: or_fn(f, fn))
