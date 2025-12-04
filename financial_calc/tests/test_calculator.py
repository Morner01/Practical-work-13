import pytest

from calculator import calculate_simple_interest, calculate_compound_interest, calculate_tax

def test_calculate_simple_interest():
    assert calculate_simple_interest(2000, 5, 10) == 1000.0
    assert calculate_simple_interest(0, 10, 5) == 0.0
    with pytest.raises(ValueError):
        calculate_simple_interest(-2000, 5, 10)

def test_calculate_compound_interest():
    assert calculate_compound_interest(2000, 5, 10, 2) == 3277.2328805807883
    assert calculate_compound_interest(2000, 0, 10, 2) == 2000.0
    with pytest.raises(ValueError):
        calculate_compound_interest(-2000, 0, 10, 2)
    with pytest.raises(ValueError):
        calculate_compound_interest(2000, 5, 10, -1)

def test_calculate_tax():
    assert calculate_tax(100, 50) == 50.0
    assert calculate_tax(0, 30) == 0.0
    with pytest.raises(ValueError):
        calculate_tax(1, 101)
    with pytest.raises(ValueError):
        calculate_tax(1, -1)