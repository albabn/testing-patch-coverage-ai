#!/usr/bin/env python3

def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulo(a, b):
    """Calculate the remainder when a is divided by b."""
    if b == 0:
        raise ValueError("Cannot calculate modulo with zero")
    return a % b


def power(a, b):
    """Raise a to the power of b."""
    return a ** b


def absolute_value(a):
    """Return the absolute value of a number."""
    if a < 0:
        return -a
    return a


def maximum(a, b):
    """Return the maximum of two numbers."""
    if a > b:
        return a
    return b


def minimum(a, b):
    """Return the minimum of two numbers."""
    if a < b:
        return a
    return b


def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0


def is_odd(n):
    """Check if a number is odd."""
    return n % 2 != 0


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

