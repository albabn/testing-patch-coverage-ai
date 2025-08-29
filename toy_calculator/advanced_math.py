#!/usr/bin/env python3


def square(a):
    """Calculate the square of a number."""
    return a ** 2


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


if __name__ == "__main__":
    # Example usage when run as script
    print("🚀 Advanced Math Functions Demo")
    print("=" * 40)
    
    # Test the square function
    print(f"5² = {square(5)}")
    print(f"3² = {square(3)}")
    print(f"10² = {square(10)}")
    
    # Test the new functions
    print(f"\n5³ = {cube(5)}")
    print(f"2⁴ = {power(2, 4)}")
    print(f"5! = {factorial(5)}")
    
    print("\n✨ All advanced math functions are ready to use!")





