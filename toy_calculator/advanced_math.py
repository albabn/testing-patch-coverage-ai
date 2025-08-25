#!/usr/bin/env python3

import math
def square(a):
    """Calculate the square of a number."""
    return a ** 2


def square_root(a):
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)





