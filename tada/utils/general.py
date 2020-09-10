from .functional import identity, curry


@curry(3)
def and_fn(fx, fy, a, *args, **kwargs):
    """
    calls given fx and fy by given arguments,
    if both fx and fy result are equivalent to true in boolean,
    then returns fy result,
    otherwise returns result of one which failed
    """
    return fx(a, *args, **kwargs) and fy(a, *args, **kwargs)


@curry(3)
def or_fn(fx, fy, a, *args, **kwargs):
    """
    call fx with given arguments,
    if fx result boolean equivalent is true,
    then returns the result of fx and fy won't be called,
    otherwise calls fy with same arguments and return its result
    """
    return fx(a, *args, **kwargs) or fy(a, *args, **kwargs)


@curry(2)
def prop(attr, obj):
    """ returns obj.*attr* (same as getattr(attr, obj)) """
    return getattr(attr, obj)


@curry(4)
def apply_if_else(constraint, if_fn, else_fn, obj):
    """
    if constraint(obj),
    then returns if_fn(obj),
    otherwise returns else_fn(obj)
    """
    return if_fn(obj) if constraint(obj) else else_fn(obj)


@curry(3)
def apply_if(constraint, fn, obj):
    """
    if constraint(obj),
    then returns if_fn(obj),
    otherwise returns obj
    """
    return apply_if_else(constraint, fn, identity, obj)
