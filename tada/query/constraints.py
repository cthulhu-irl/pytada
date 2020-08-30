class Constraint(object):

    def __init__(self, fn, *args, **kwargs):
        pass

    def __call__(self, obj):
        pass

    def __and__(self, other):
        return self.and(other)

    def __or__(self, other):
        return self.or(other)

    def __xor__(self, other):
        return self.xor(other)

    def match(self, obj):
        pass

    def and(self, other):
        pass

    def or(self, other):
        pass

    def xor(self, other):
        pass

