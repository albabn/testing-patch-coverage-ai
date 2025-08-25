import math


def square(a):
    """Calculate the square of a number."""
    return a ** 2


def square_root(a):
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)


def power(a, b):
    """Calculate a raised to the power of b."""
    return a ** b


def cube(a):
    """Calculate the cube of a number."""
    return a ** 3 