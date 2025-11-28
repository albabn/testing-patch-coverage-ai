import pytest
from calculator import (
    absolute_value,
    add,
    divide,
    factorial,
    is_even,
    is_odd,
    maximum,
    minimum,
    modulo,
    multiply,
    power,
    subtract,
)


def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0


def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5
    assert subtract(3.5, 1.5) == 2.0


def test_multiply():
    """Test the multiply function."""
    assert multiply(4, 5) == 20
    assert multiply(-2, 3) == -6


def test_divide():
    """Test division logic including divide-by-zero."""
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3
    with pytest.raises(ValueError):
        divide(5, 0)


def test_modulo():
    """Test modulo calculations and zero guard."""
    assert modulo(10, 3) == 1
    assert modulo(9, 3) == 0
    with pytest.raises(ValueError):
        modulo(5, 0)


def test_power():
    """Test exponentiation."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_absolute_value():
    """Test absolute value for positive and negative inputs."""
    assert absolute_value(-7) == 7
    assert absolute_value(4) == 4


def test_maximum():
    """Test maximum selection for both branches."""
    assert maximum(10, 5) == 10
    assert maximum(-1, 3) == 3


def test_minimum():
    """Test minimum selection for both branches."""
    assert minimum(10, 5) == 5
    assert minimum(-1, 3) == -1


def test_is_even_and_is_odd():
    """Test parity helpers."""
    assert is_even(4)
    assert not is_even(5)
    assert is_odd(5)
    assert not is_odd(4)


def test_factorial_cases():
    """Test factorial for base, iterative, and error scenarios."""
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

