""" functional programming utilities """


def identity(x):
    """ always return what's given """
    return x


def curry(arg_count):
    """ function decorator for currying function's arguments """
    fn_args = []
    fn_kwargs = {}

    def _decorator(fn):
        def _currier(*args, **kwargs):
            fn_args.extend(args)
            fn_kwargs.update(kwargs)

            if len(fn_args) >= arg_count:
                return fn(*fn_args, **fn_kwargs)

        return _currier

    return _decorator


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

    def _composer(*args, **kwargs):
        if fns:
            first, *rest = fns
            return f(compose(g, first, *rest)(*args, **kwargs))

        return f(g(*args, **kwargs))

    return _composer


@curry(2)
def fmap(fn, obj):
    """
    maps the given obj to given fn through obj's map method
    """
    return obj.map(fn)
