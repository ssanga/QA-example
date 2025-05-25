import sys
import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator
import pytest

calc = Calculator()

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_subtract():
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(0, 3) == -3

def test_multiply():
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(-2, 3) == -6

def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(-6, 3) == -2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_power():
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(9, 0.5) == pytest.approx(3)
    assert calc.power(-2, 3) == -8
    assert calc.power(4, -1) == pytest.approx(0.25)