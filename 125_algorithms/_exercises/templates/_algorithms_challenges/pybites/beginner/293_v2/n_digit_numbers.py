from typing import List, TypeVar
import math
T = TypeVar('T', int, float)


___ n_digit_numbers(numbers: List[T], n: int) -> List[int]:

    __ n < 1:
        raise ValueError

    

    return [int(number *10**(n -1)) __ number < 10**(n-1) else int(number / 10**(math.floor(math.log(abs(number),10)) + 1 -n )) __ number > 10**(n -1) else int(number) for number in numbers]

