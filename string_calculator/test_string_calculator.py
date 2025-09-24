import pytest
from string_calculator import StringCalculator

def test_add_empty_string_returns_zero():
    calculator = StringCalculator()
    assert calculator.add("") == 0

def test_add_single_number_returns_number():
    calculator = StringCalculator()
    assert calculator.add("1") == 1
    assert calculator.add("5") == 5
    
def test_add_two_numbers_comma_separated_returns_sum():
    calculator = StringCalculator()
    assert calculator.add("1,2") == 3
    assert calculator.add("5,7") == 12
    assert calculator.add("0,0") == 0

def test_add_unknown_amount_of_numbers_returns_sum():
    calculator = StringCalculator()
    assert calculator.add("1,2,3") == 6
    assert calculator.add("10,20,30,40") == 100
    assert calculator.add("1,2,3,4,5,6,7,8,9,10") == 55