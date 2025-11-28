#!/usr/bin/env python3


def square(a):
    """Calculate the square of a number."""
    return a ** 2


def cube(a):
    """Calculate the cube of a number."""
    return a ** 3


def square_root(a):
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5


def average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def median(numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    return sorted_numbers[n//2]


if __name__ == "__main__":
    # Example usage when run as script
    print("🚀 Advanced Math Functions Demo")
    print("=" * 30)
    
    # Test the square function
    print(f"5² = {square(5)}")
    print(f"3² = {square(3)}")
    print(f"10² = {square(10)}")
    
    # Test the cube function
    print(f"\n5³ = {cube(5)}")
    print(f"3³ = {cube(3)}")
    
    # Test average
    print(f"\nAverage of [1, 2, 3, 4, 5] = {average([1, 2, 3, 4, 5])}")
    
    print("\n✨ Advanced math functions are ready to use!")





