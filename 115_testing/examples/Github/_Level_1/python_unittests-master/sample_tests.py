import pytest 
import sample_functions


def test_sum():
    num1 = 5
    num2 = 10
    expected = 15
    assert sample_functions.sum(num1, num2) == 15

def test_contains_numbers():
    input_str = "el12lk3j5mnfadf"
    assert sample_functions.contains_numbers(input_str) == True

def test_does_not_contain_numbers():
    input_str = "lkqwjqlkjlkjed"
    assert sample_functions.contains_numbers(input_str) == False

def test_div():
    num1 = 10
    num2 = 5
    expected = 2
    assert sample_functions.div(num1, num2) == expected

def test_div_by_zero():
    num1 = 10
    num2 = 0
    with pytest.raises(ZeroDivisionError):
        sample_functions.div(num1, num2)


#Create separate and independent test cases
#For instance, avoid this:
def test_div2():
    num1 = 10
    num2 = 5
    expected = 2
    assert sample_functions.div(num1, num2) == expected
    num2 = 0
    with pytest.raises(ZeroDivisionError):
        sample_functions.div(num1, num2)
#Two aspects being tested under the same test case. Not a good practice.