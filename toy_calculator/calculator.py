#!/usr/bin/env python3

def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b



def cube(a):
    """Calculate the cube of a number."""
    return a ** 3


def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base ** exponent


def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result