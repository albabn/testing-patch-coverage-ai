import pytest
from calculator import add, cube, factorial, power, subtract


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


def test_cube():
    """Test the cube function."""
    assert cube(3) == 27
    assert cube(-2) == -8


def test_power():
    """Test the power function."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_factorial():
    """Test the factorial function including edge cases and errors."""
    with pytest.raises(ValueError) as excinfo:
        factorial(-1)
    assert "not defined" in str(excinfo.value)

    assert factorial(0) == 1
    assert factorial(1) == 1

    assert factorial(5) == 120

