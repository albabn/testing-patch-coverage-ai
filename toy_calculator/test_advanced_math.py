import runpy

import pytest
from advanced_math import cube, factorial, power, square


def test_square():
    assert square(5) == 25
    assert square(0) == 0
    assert square(-3) == 9


def test_cube():
    assert cube(2) == 8
    assert cube(-2) == -8


def test_power():
    assert power(2, 4) == 16
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5


def test_factorial_values():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


def test_module_as_script_outputs(capsys):
    runpy.run_module("advanced_math", run_name="__main__")
    out = capsys.readouterr().out
    assert "Advanced Math Functions Demo" in out
    assert "5² = 25" in out
    assert "2⁴ = 16" in out
    assert "5! = 120" in out
