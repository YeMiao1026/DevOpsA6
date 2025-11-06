import pytest

from myapp import add, divide


def test_add():
    assert add(1, 2) == 3


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
