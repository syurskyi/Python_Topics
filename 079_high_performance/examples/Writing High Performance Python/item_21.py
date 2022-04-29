import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
def safe_division(number, divisor, ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# Example 2
result = safe_division(1.0, 10**500, True, False)
print(result)
assert result is 0


# Example 3
result = safe_division(1.0, 0, False, True)
print(result)
assert result == float('inf')


# Example 4
def safe_division_b(number, divisor,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# Example 5
assert safe_division_b(1.0, 10**500, ignore_overflow=True) is 0
assert safe_division_b(1.0, 0, ignore_zero_division=True) == float('inf')


# Example 6
assert safe_division_b(1.0, 10**500, True, False) is 0


# Example 7
def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# Example 8
try:
    safe_division_c(1.0, 10**500, True, False)
except:
    logging.exception('Expected')
else:
    assert False


# Example 9
safe_division_c(1.0, 0, ignore_zero_division=True)  # No exception
try:
    safe_division_c(1.0, 0)
    assert False
except ZeroDivisionError:
    pass  # Expected
