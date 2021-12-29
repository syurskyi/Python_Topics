from typing import List, TypeVar
T = TypeVar('T', int, float)


___ n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    number_list = []
    __ n == 0:
        raise ValueError
    for number in numbers:
        __ number == 0:
            number_list.append(0)
        number_of_digits = len(str(number).replace('.', ''))
        __ number >= 1:
            __ number_of_digits <= n:
                number_list.append(int(str(number * 10 **n)[:n]))
            elif number_of_digits >= n:
                number_list.append(int(str(number * 10 **n)[:n]))
        __ number <= -1:
            __ number_of_digits <= n:
                number_list.append(int(str(number * 10 **n)[:n + 1]))
            elif number_of_digits > n:
                number_list.append(int(str(number * 10 **n)[:n + 1]))
            else:
                number_list.append(number)
    return number_list