from ..utils.funcional import identity
from ..utils.general import and_fn, or_fn, xor_fn

class Query(object):

    def __init__(self, selector=identity):
        self.fn = selector

    #-- syntactic sugar

    def __call__(self, obj):
        return self.query(obj)

    def __lshift__(self, selector):
        return self.then(query)

    def __and__(self, selector):
        return self.and_(selector)

    def __or__(self, selector):
        return self.or_(selector)

    def __xor__(self, selector):
        return self.xor_(selector)

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

    #-- helpers

    def and_(self, selector):
        return self.map(lambda fn: and_fn(fn, selector))

    def or_(self, selector):
        return self.map(lambda fn: or_fn(fn, selector))

    def xor_(self, selector):
        return self.map(lambda fn: xor_fn(fn, selector))

