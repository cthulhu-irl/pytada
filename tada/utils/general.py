from .functional import curry

@curry(2)
def prop(attr, obj):
    pass

@curry(4)
def apply_if_else(constraint, if_fn, else_fn, obj):
    pass

@curry(3)
def apply_if(constraint, fn, obj):
    pass

def fix_status(todo):
    pass
