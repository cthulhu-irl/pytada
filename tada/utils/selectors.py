from functools import cmp_to_key

from .functional import curry


@curry(2)
def forall(fn, arr):
    """
    checks if all items in array conform to given fn
    by passing the item to fn and checking the result as boolean
    """
    return all(fn(item) for item in arr)


@curry(2)
def select(fn, arr):
    """
    returns list of items in arr which fn(item) is true for them
    """
    return [item for item in arr if fn(item)]


@curry(2)
def filter(fn, arr):
    """
    returns list of items in arr which fn(item) is false for them
    """
    return [item for item in arr if not fn(item)]


@curry(2)
def offset(count, arr):
    """
    returns arr[count-1:], so counting from 1 instead of 0
    """
    return arr[count-1:]


@curry(2)
def limit(count, arr):
    """ returns arr[:count] """
    return arr[:count]


@curry(3)
def slice(start, end, arr):
    """ return arr[start:end] """
    return arr[start:end]


@curry(2)
def sort(fn, arr):
    """ sorts the given array according to given function """
    return sorted(arr, key=cmp_to_key(fn))


def unique(arr):
    """ returns arr without duplicates """
    unique_arr = []
    for item in arr:
        if item not in unique_arr:
            unique_arr.append(item)

    return unique_arr
