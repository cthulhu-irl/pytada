from functools import wraps

def identity(x):
    """ always return what's given """
    return x


class curry(object):

    def __init__(self, arity, *args, **kwargs):
        self.arity = arity
        self.args = args
        self.kwargs = kwargs

    def __call__(self, fn):
        self.fn = fn
        return self.currier

    def of(self, fn, arity, *args, **kwargs):
        return self.__class__(arity, *args, **kwargs)(fn)

    def currier(self, *args, **kwargs):
        args = list(args)
        arity = self.arity - len(args)

        args.extend(self.args)
        kwargs.update(self.kwargs)

        if arity <= 0:
            return self.fn(*args, **kwargs)

        return self.of(self.fn, arity, *args, **kwargs)


@curry(2)
def compose(f, g, *fns):
    """
    composes given functions together as when the returned
    function called, the given arguments would go to last
    given function, and then the result of last given
    function is passed as argument to the given function
    before last one... and this goes up until the first,
    then the result is returned.
    """

    for fn in fns:
        g = compose(g, fn)

    def _composed(*args, **kwargs):
        return f(g(*args, **kwargs))

    return _composed


@curry(2)
def fmap(fn, obj):
    """
    maps the given obj to given fn through obj's map method
    """
    return obj.map(fn)
