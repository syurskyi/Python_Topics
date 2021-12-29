"""
In this bite you learn to catch/raise exceptions.

Write a simple division function meeting the following requirements:

when denominator is 0 catch the corresponding exception and return 0.
when numerator or denominator are not of the right type reraise the corresponding exception.
if the result of the division (after surviving the exceptions) is negative, raise a ValueError
As always see the tests written in pytest to see what your code need to pass. Have fun!

"""
def my_solution_positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return 0
    except:
        raise
    if result < 0:
        raise ValueError
    return result

print(my_solution_positive_divide(1,2))

"""
Interesting difference between my solution and pybites solution is how
try-else clause is used. I did not know that this might make any difference:
https://stackoverflow.com/questions/855759/python-try-else

But I think that in this particular case, it doesn't really matter.
If there was no exception, we check result variable and return if no exception...

"""

def pybites_solution_positive_divide(numerator, denominator):
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        return 0
    except (TypeError, ValueError):
        raise
    else:
        if result < 0:
            raise ValueError('Cannot be negative')
        return result