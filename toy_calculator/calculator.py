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
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def increment(a):
    """Increment a number by 1."""
    return a + 1


def decrement(a):
    """Decrement a number by 1."""
    return a - 1


def power(a, b):
    """Calculate a raised to the power of b."""
    return a ** b