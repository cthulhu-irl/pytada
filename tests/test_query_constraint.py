from tada.query import constraints as cs
from tada.query.constraint import Constraint as C

def test_intersects():
    assert cs.intersects(['b', 'c', 'g'], 'abcd')
    assert cs.intersects('ab', 'abcd')
    assert cs.intersects([0], [0])

    assert not cs.intersects([], [])
    assert not cs.intersects('', '')
    assert not cs.intersects([1, 2], [3, 4])
    assert not cs.intersects('abc', 'efg')

def test_starts_with():
    assert cs.starts_with('abcd', 'abcd')
    assert cs.starts_with('ab', 'abcd')
    assert cs.starts_with('', 'abcd')
    assert cs.starts_with('', '')
    assert cs.starts_with([1], [1, 2, 3])
    assert cs.starts_with([1, 2, 3], [1, 2, 3])
    assert cs.starts_with([], [1, 2, 3])
    assert cs.starts_with([], [])

    assert not cs.starts_with('ac', 'abcd')
    assert not cs.starts_with('bc', 'abcd')
    assert not cs.starts_with([2, 3], [1, 2, 3])
    assert not cs.starts_with([4, 5], [1, 2, 3])
    assert not cs.starts_with([1, 3], [1, 2, 3])

def test_ends_with():
    assert cs.ends_with('abcd', 'abcd')
    assert cs.ends_with('cd', 'abcd')
    assert cs.ends_with('', 'abcd')
    assert cs.ends_with('', '')
    assert cs.ends_with([3], [1, 2, 3])
    assert cs.ends_with([1, 2, 3], [1, 2, 3])
    assert cs.ends_with([], [1, 2, 3])
    assert cs.ends_with([], [])

    assert not cs.ends_with('bd', 'abcd')
    assert not cs.ends_with('dc', 'abcd')
    assert not cs.ends_with('e', 'abcd')
    assert not cs.ends_with([1, 2], [1, 2, 3])
    assert not cs.ends_with([4, 5], [1, 2, 3])
    assert not cs.ends_with([1, 3], [1, 2, 3])

def test_and_composition():
    contains = cs.contains

    contains_ab = C(contains('a')) & C(contains('b'))
    contains_ef = C(contains('e')) & C(contains('f'))

    obj = 'abcd'

    result = contains('a', obj) and contains('b', obj)
    assert result == contains_ab(obj)

    result = contains('e', obj) and contains('f', obj)
    assert result == contains_ef(obj)

def test_or_composition():
    contains = cs.contains

    contains_ef = C(contains('e')) | C(contains('f'))
    contains_ed = C(contains('e')) | C(contains('d'))

    obj = 'abcd'

    result = contains('e', obj) or contains('f', obj)
    assert result == contains_ef(obj)

    result = contains('e', obj) or contains('d', obj)
    assert result == contains_ed(obj)
