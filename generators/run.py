"""Generators are special functions which is capable of resuming where a function
left off(typically a 'return') with the help of 'yield' keyword.
Any function containing 'yield'(even with 'return') in its body is a 'generator function'.

This program creates a generator function which simply yields 'n' numbers.

Note that generator iterator(or more generally generator) is a special type of iterator.
"""

def generate_sequence():

    i = 0
    for i in range(10):
        yield i


if __name__ == '__main__':

    print(generate_sequence)
    print(generate_sequence())

    """Generators can be used either using for-in loop(since they are essentially iterators)
    or using next() method
    """

    for i in generate_sequence():
        print(i)
