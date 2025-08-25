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


if __name__ == "__main__":
    # Example usage when run as script
    print("🧮 Calculator Demo")
    print("=" * 30)
    
    # Test basic operations
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 × 7 = {multiply(6, 7)}")
    print(f"15 ÷ 3 = {divide(15, 3)}")
    
    # Test error handling
    try:
        result = divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n✨ Calculator functions are ready to use!") 