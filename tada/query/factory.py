from .query import Query as Q
from ..utils.functional import identity, compose
from ..utils.selectors import select
from ..utils.constraints import contains


class QueryFactory(object):
    """
    make query from other representations by given registry
    of selectors and a default selector for when
    a selector is not found.
    """

    DELIMITER = ':'

    def __init__(self, registry={}, default=None):
        self.registry = registry.copy()
        self.default = (
            default or compose(select, contains),
            False
        )
        self.max_depth = 1000

    def _parse_clause(self, s):
        """
        if given string has only one delimiter,
        divides it and returns,
        otherwise returns a tuple containing two of the string.
        """
        delim = self.DELIMITER

        if delim in s and s.index(delim) == s.rindex(delim):
            ret = s.split(delim)
            if not self._isinfix(ret[0]):
                return ret

        return (s, s)

    def _reclause(self, a, b):
        """
        makes a string clause out of a and b with delimiter
        """
        return f'{a}{self.DELIMITER}{b}'

    def _get_handler(self, fname):
        """
        returns the registered handler tuple of
        function (a -> b) and its type converter function
        if fname found in registry, otherwise returns the
        default handler.
        """
        return self.registry.get(fname, self.default)

    def _isinfix(self, fname):
        return self._get_handler(fname)[1]

    def _infix_list_composer(
        self,
        lst,
        sofar=Q(identity),
        *,
        depth=100
    ):
        """
        converts given clauses into selectors and composes
        ones with parameter together and calls the ones
        which are infix by composed left ones and composed
        right ones and returns the result of that call.
        """

        if not lst or depth <= 0:
            return sofar

        (fname, farg), *rest = lst
        fn, isinfix = self._get_handler(fname)

        if isinfix:
            sogoing = self._infix_list_composer(
                rest, Q(identity), depth=depth-1
            )
            return Q(fn(sofar, sogoing))

        try:
            fx = fn(farg)
        except Exception:
            fx = self.default[0](self._reclause(fname, farg))

        sofar = sofar.then(fx)

        return self._infix_list_composer(
            rest, sofar, depth=depth-1
        )

    def register(self, fn, isinfix=False, fname=''):
        """
        adds a handler (tuple(fn, ft)) to registry
        of given fname or the fn's name if fname isn't given.
        """
        self.registry[fname or fn.__qualname__] = (fn, isinfix)

    def unregister(self, fname):
        """ pops fname handler out of registry """
        self.registery.pop(fname, None)

    def fromstr(self, string):
        """ makes a Query out of given query string """
        lst = map(lambda s: s.strip(), string.split())
        lst = map(self._parse_clause, lst)
        q = self._infix_list_composer(lst, depth=self.max_depth)

        return q
