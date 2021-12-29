from typing import List, TypeVar
import math

T = TypeVar('T', int, float)


def n_digit_number(number: T, n: int) -> int:
    '''converts number to an n-digit int, preserving sign'''
    sign = -1 if number < 0 else 1
    num = abs(number)
    dexp = n - int(math.log10(num)) - 1 if num !=0 else 0
    res = num * 10**(dexp)
    return int(sign * res)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError
    return list(map(lambda x: n_digit_number(x, n), numbers))
