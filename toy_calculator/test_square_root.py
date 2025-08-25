import pytest
from calculator import square_root


def test_square_root_positive():
    assert square_root(0) == 0
    assert square_root(4) == 2


def test_square_root_negative():
    with pytest.raises(
        ValueError, match="Cannot calculate square root of negative number"
    ):
        square_root(-1)
