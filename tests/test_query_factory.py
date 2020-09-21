from tada.query.query import Query as Q
from tada.query.factory import QueryFactory
from tada.utils.functional import identity, compose
from tada.utils.selectors import select, filter, offset, limit
from tada.utils.constraints import contains, starts_with

handlers = {
    'OR': (Q.or_, True),
    'AND': (Q.and_, True),
    'offset': (compose(offset, int), False),
    'limit': (compose(limit, int), False),
    'startswith': (compose(select, starts_with), False),
    'filter': (compose(filter, contains), False)
}
qf = QueryFactory(handlers)

def test_fromstr_default():
    q = qf.fromstr('x or y')
    assert q(['a', 'b', 'c']) == []
    assert q(['x', 'y', 'x']) == []
    assert q(['x', 'y', 'or']) == ['x', 'y', 'or']

def test_fromstr_infix():
    q = qf.fromstr('x OR y')
    assert q(['a', 'b', 'c']) == []
    assert q(['x', 'b', 'c']) == ['x']
    assert q(['x', 'x', 'y']) == ['x', 'x', 'y']
    assert q(['x', 'y', 'OR']) == ['x', 'y']

def test_fromstr_fall_type_error_to_default():
    q = qf.fromstr('offset:blah')
    assert q(['a', 'offset:blah']) == ['offset:blah']

def test_fromstr_infix_with_parameter():
    q = qf.fromstr('a OR:2 b')
    assert q(['a', 'c']) == ['a']
    assert q(['c', 'b']) == ['b']
    assert q(['c', 'OR:2']) != ['OR:2']

def test_fromstr_order():
    q = qf.fromstr('limit:4 offset:2')
    assert q([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 3, 4]

    q = qf.fromstr('offset:2 limit:4')
    assert q([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 3, 4, 5]
