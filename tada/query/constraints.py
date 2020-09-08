from ..utils.general import and_fn, or_fn, xor_fn

class Constraint(object):
    '''
    logically composable contraint wrapper by infix operators.
    '''

    def __init__(self, fn):
        self.fn = fn

    #-- syntactic sugar

    def __call__(self, *args, **kwargs):
        return self.match(*args, **kwargs)

    def __and__(self, other):
        return self.and_(other)

    def __or__(self, other):
        return self.or_(other)

    def __xor__(self, other):
        return self.xor_(other)

    #-- functor

    def map(self, fn):
        return self.__class__(fn(self.fn))

    def join(self):
        return self.fn

    #-- functionality

    def match(self, *args, **kwargs):
        '''
        calls beneath constraint function and returns result.
        '''
        return self.fn(*args, **kwargs)

    #-- logical combinations

    def and_(self, other):
        '''
        compose with another constraint by and logical function.
        it is same as and_fn(self, other) but returning
        a constraint instance.
        '''
        return self.map(lambda f: and_fn(f, other))

    def or_(self, other):
        '''
        compose with another constraint by or logical function.
        it is same as or_fn(self, other) but returning
        a constraint instance.
        '''
        return self.map(lambda f: or_fn(f, other))

    def xor_(self, other):
        '''
        compose with another constraint by xor logical function.
        it is same as xor_fn(self, other) but returning
        a constraint instance.
        '''
        return self.map(lambda f: xor_fn(f, other))

