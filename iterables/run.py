"""Iterable is any object which can be looped over in Python.
It can be either a sequence(list, str, tuple) or any non-sequence object such as
dict, set.

This program shows how for loops in Python are actually implemented i.e how universally
iterables are looped over using the 'for in' statement.
"""


if __name__ == '__main__':

    """Create a sequence(list) with 10 numbers"""
    a = list(range(10))
    b = {1, 2, 3}
    print(b)

    """An iterable object can be looped over using an 'Iterator'. Iterator is used
    to perform one-pass over the iterable object.
    1. To create an iterator, call iter() on the iterable object.
    2. To fetch an item, call next() on the iterator.
    """
    itr = iter(b)
    print(itr)

    while True:
        try:
            item = next(itr)
        except StopIteration:
            break
        print(item)
