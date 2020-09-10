from .base import LogicallyComposable


class Constraint(LogicallyComposable):
    """
    logically composable contraint wrapper by infix operators.
    """

    def __init__(self, fn):
        self.fn = fn

    # syntactic sugar

    def __call__(self, *args, **kwargs):
        return self.match(*args, **kwargs)

    # functor

    def map(self, fn):
        return self.__class__(fn(self.fn))

    def join(self):
        return self.fn

    # functionality

    def match(self, *args, **kwargs):
        """
        calls beneath constraint function and returns result.
        """
        return self.fn(*args, **kwargs)
