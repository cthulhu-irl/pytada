from functools import cmp_to_key

from .functional import curry

@curry(2)
def forall(fn, arr):
    return all(fn(item) for item in arr)

@curry(2)
def select(fn, arr):
    return [item for item in arr if fn(item)]

@curry(2)
def filter(fn, arr):
    return [item for item in arr if not fn(item)]

@curry(2)
def offset(index, arr):
    return arr[index:]

@curry(2)
def limit(count, arr):
    return arr[:count]

@curry(3)
def slice(start, end, arr):
    return arr[start:end]

@curry(2)
def sort(fn, arr):
    return sorted(arr, key=cmp_to_key(fn))

def unique(arr):
    unique_arr = []
    for item in arr:
        if item not in unique_arr:
            unique_arr.append(item)

    return unique_arr

