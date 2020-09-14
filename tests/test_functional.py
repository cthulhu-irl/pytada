from tada.utils.functional import identity, curry, compose

def test_identity():
    assert identity(1) == identity(1)
    assert identity('2') == identity('2')
    assert identity([3]) == identity([3])
    assert identity(identity) == identity(identity)

def test_curry():
    fn = lambda a, b, c: a * b * c
    assert curry(3)(fn)(1, 2, 3) == fn(1, 2, 3)
    assert curry(3)(fn)(1)(2)(3) == fn(1, 2, 3)
    assert curry(3)(fn)(1, 2)(3) == fn(1, 2, 3)

def test_compose():
    fn = lambda a: a ** 2
    fx = compose(fn, identity)
    fy = compose(identity, fn)

    assert fx(3) == fy(3) == fn(3)

    assert compose(fn, fn, fn)(2) == fn(fn(fn(2)))
