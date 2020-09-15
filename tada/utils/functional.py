""" functional programming utilities """


def identity(x):
    """ always return what's given """
    return x


def curry(arg_count):
    """ function decorator for currying function's arguments """

    def _decorator(fn):

        def _holder(*args, **kwargs):
            fn_args = []
            fn_kwargs = {}

            def _currier(*args, **kwargs):
                fn_args.extend(args)
                fn_kwargs.update(kwargs)

                if len(fn_args) >= arg_count:
                    cp_args = fn_args[:]
                    cp_kwargs = fn_kwargs.copy()

                    fn_args.clear()
                    fn_kwargs.clear()

                    return fn(*cp_args, **cp_kwargs)

                return _currier

            return _currier(*args, **kwargs)

        return _holder

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
