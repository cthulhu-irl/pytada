from .functional import identity, curry

@curry(2)
def prop(attr, obj):
    return getattr(attr, obj)

@curry(4)
def apply_if_else(constraint, if_fn, else_fn, obj):
    return if_fn(obj) if constraint(obj) else else_fn(obj)

@curry(3)
def apply_if(constraint, fn, obj):
    return apply_if_else(constraint, fn, identity, obj)

def fix_status(todo):
    pass
