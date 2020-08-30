from ..utils.funcional import identity

class Query(object):

    def __init__(self, selector=identity):
        pass

    #-- syntactic sugar

    def __lshift__(self, query):
        pass

    def __rshift__(self, selector):
        pass

    def __or__(self, obj):
        pass

    #-- functor

    def map(self, fn):
        pass

    def join(self):
        pass

    #-- functionality

    def extend(self, query):
        pass

    def then(self, selector):
        pass

    def query(self, obj):
        pass

    #-- helpers

    def and(self, selector):
        pass

    def or(self, selector):
        pass

    def xor(self, selector):
        pass

