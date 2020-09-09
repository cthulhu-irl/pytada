from .functional import identity, curry

@curry(3)
def and_fn(fx, fy, a, *args, **kwargs):
    return fx(a, *args, **kwargs) and fy(a, *args, **kwargs)

@curry(3)
def or_fn(fx, fy, a, *args, **kwargs):
    return fx(a, *args, **kwargs) or fy(a, *args, **kwargs)

@curry(2)
def prop(attr, obj):
    return getattr(attr, obj)

@curry(4)
def apply_if_else(constraint, if_fn, else_fn, obj):
    return if_fn(obj) if constraint(obj) else else_fn(obj)

@curry(3)
def apply_if(constraint, fn, obj):
    return apply_if_else(constraint, fn, identity, obj)

