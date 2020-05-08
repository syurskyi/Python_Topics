import pytest

___ fizzBuzz( value ):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)

___ isMultiple( value, mod ):
    return (value % mod) == 0

___ checkFizzBuzz( value, expectedRetVal ):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal

___ test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

___ test_returns2With2PassedIn():
    checkFizzBuzz(2, "2")

___ test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

___ test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

___ test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")

___ test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

___ test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")
