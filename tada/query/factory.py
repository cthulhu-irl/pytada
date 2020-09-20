from .query import Query as Q
from ..utils.functional import identity, curry, compose
from ..utils.selectors import select
from ..utils.constraints import contains

class QueryFactory(object):
    FUNC = 0
    TYPE = 1

    DELIMITER = ':'

    def __init__(self, registry={}, default=None):
        self.registry = registry.copy()
        self.default = (
            default or compose(select, contains),
            identity
        )
        self.max_depth = 1000

    def _argconvert(self, fname, arg):
        return self.registry[fname][self.TYPE](arg)

    def _parse_clause(self, s):
        delim = self.DELIMITER

        if delim in s and s.index(delim) == s.rindex(delim):
            return s.split(delim)

        if not self._isinfix(s):
            return (s, s)

        return s

    def _isinfix(self, x):
        return isinstance(x, str) and x in self.registry

    def _get_handler(self, fname):
        return self.registry.get(fname, self.default)

    def _infix_list_composer(
        self,
        lst,
        sofar=identity,
        *,
        depth=100
    ):
        if not lst or depth <= 0:
            return sofar

        first, *rest = lst
        fn, ft = self._get_handler(
            first if self._isinfix(first) else first[0]
        )

        if self._isinfix(first):
            sogoing = self._infix_list_composer(
                rest, identity, depth=depth-1
            )
            return fn(ft(sofar), ft(sogoing))

        print("%s(%s)" % (first[0], first[1]))
        sofar = compose(sofar, fn(ft(first[1])))

        return self._infix_list_composer(
            rest, sofar, depth=depth-1
        )

    def register(self, fn, ft, fname=''):
        self.registry[fname or fn.__qualname__] = (fn, ft)

    def unregister(self, fname):
        self.registery.pop(fname, None)

    def fromstr(self, string):
        lst = map(lambda s: s.strip(), string.split())
        lst = map(self._parse_clause, lst)
        f = self._infix_list_composer(lst, depth=self.max_depth)

        return Q(f)
