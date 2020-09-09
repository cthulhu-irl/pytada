from .base import LogicallyComposable
from ..utils.funcional import identity

class Query(LogicallyComposable):

    def __init__(self, selector=identity):
        self.fn = selector

    #-- syntactic sugar

    def __call__(self, obj):
        return self.query(obj)

    def __lshift__(self, selector):
        return self.then(query)

    #-- functor

    def map(self, fn):
        return self.__class__(fn(self.fn))

    def join(self):
        return self.fn

    #-- functionality

    def then(self, selector):
        return self.map(compose(selector))

    def query(self, obj):
        return self.fn(obj)

