from .base import LogicallyComposable
from ..utils.functional import identity, compose


class Query(LogicallyComposable):
    """
    logically composable container for query functions
    with ability to mix with other query instances

    this class' instances are also callable which
    makes them to be potentially a selector function
    with only one argument
    """

    def __init__(self, selector=identity, *, composer=compose):
        self.fn = selector
        self.composer = composer

    # syntactic sugar

    def __call__(self, obj):
        return self.query(obj)

    def __lshift__(self, selector):
        return self.then(selector)

    # functor

    def map(self, fn):
        return self.__class__(fn(self.fn))

    def join(self):
        return self.fn

    # functionality

    def then(self, selector):
        """
        compose the given selector with inner selector
        and return a new instance
        """
        return self.map(self.composer(selector))

    def query(self, obj):
        """ apply the inner query on given obj """
        return self.fn(obj)
