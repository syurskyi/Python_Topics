from typing import List, TypeVar

T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    number_list = []
    if n == 0:
        raise ValueError
    for number in numbers:
        if number == 0:
            number_list.append(0)
        number_of_digits = len(str(number).replace('.', ''))
        if number >= 1:
            if number_of_digits <= n:
                number_list.append(int(str(number * 10 **n)[:n]))
            elif number_of_digits >= n:
                number_list.append(int(str(number * 10 **n)[:n]))
        if number <= -1:
            if number_of_digits <= n:
                number_list.append(int(str(number * 10 ** (n))[:n + 1]))
            elif number_of_digits > n:
                number_list.append(int(str(number * 10 ** (n))[:n + 1]))
            else:
                number_list.append(number)
    return number_list