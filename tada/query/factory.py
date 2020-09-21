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
            identity
        )
        self.max_depth = 1000

    def _parse_clause(self, s):
        """
        if given string has only one delimiter,
        divides it and returns,
        otherwise if it's not infix,
        returns a tuple containing two copies of the string,
        otherwise returns it as a (infix) string.
        """
        delim = self.DELIMITER

        if delim in s and s.index(delim) == s.rindex(delim):
            return s.split(delim)

        if s in self.registry:
            return (s, '')

        return (s, s)

    def _get_handler(self, fname):
        """
        returns the registered handler tuple of
        function (a -> b) and its type converter function
        if fname found in registry, otherwise returns the
        default handler.
        """
        return self.registry.get(fname, self.default)

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

        takes a list of clauses, if not infix,
        then calls them with given parameter after
        converting it by given type converter in registry
        and composes them,
        otherwise, recurses on the rest of the list
        to get the right operand evaluated (right selector)
        and then converts the left and right selectors/operands
        by given type converter in registry,
        then calls the infix function with those
        converted operands and returns the result.
        """

        if not lst or depth <= 0:
            return sofar

        (fname, farg), *rest = lst
        fn, isinfix = self._get_handler(fname)

        if isinfix:
            sogoing = self._infix_list_composer(
                rest, depth=depth-1
            )
            return Q(fn(sofar, sogoing))

        sofar = sofar.then(fn(farg))

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
