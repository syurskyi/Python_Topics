from typing import List, TypeVar
import math
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:

    if n < 1:
        raise ValueError

    

    return [int(number *10**(n -1)) if number < 10**(n-1) else int(number / 10**(math.floor(math.log(abs(number),10)) + 1 -n )) if number > 10**(n -1) else int(number) for number in numbers]

