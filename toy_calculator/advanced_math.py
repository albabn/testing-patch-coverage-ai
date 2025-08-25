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


def power(a, b):
    """Calculate a raised to the power of b."""
    return a ** b


def cube(a):
    """Calculate the cube of a number."""
    return a ** 3


if __name__ == "__main__":
    # Example usage when run as script
    print("🚀 Advanced Math Demo")
    print("=" * 30)
    
    # Test basic operations
    print(f"5² = {square(5)}")
    print(f"√16 = {square_root(16)}")
    print(f"2³ = {cube(2)}")
    print(f"3⁴ = {power(3, 4)}")
    
    # Test error handling
    try:
        result = square_root(-4)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n✨ Advanced math functions are ready to use!") 