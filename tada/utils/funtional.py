def identity(x):
    return x

def curry(arg_count):
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

def compose(f, g, *fns):
    pass

def fmap(fn, obj):
    return obj.map(fn)
