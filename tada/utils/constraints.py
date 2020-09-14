import re

from .functional import curry


# -- string/array related constraints

@curry(2)
def contains(element, lst):
    return element in lst


@curry(2)
def intersects(lst1, lst2):
    return all(elem in lst2 for elem in lst1)


@curry(2)
def starts_with(sub, lst):
    if len(sub) > len(lst):
        return False

    for i, element in enumerate(sub):
        if lst[i] != element:
            return False

    return True


@curry(2)
def ends_with(sub, lst):
    return starts_with(sub[::-1], lst[::-1])


@curry(2)
def regex_match(regex, string):
    return bool(re.match(regex, string))


# -- comparison constraints

@curry(2)
def inrange(start, end, num):
    return start <= num <= end


@curry(2)
def eq(a, b):
    return a == b


@curry(2)
def neq(a, b):
    return a != b


@curry(2)
def lt(a, b):
    return a < b


@curry(2)
def lte(a, b):
    return a <= b


@curry(2)
def gt(a, b):
    return a > b


@curry(2)
def gte(a, b):
    return a >= b
