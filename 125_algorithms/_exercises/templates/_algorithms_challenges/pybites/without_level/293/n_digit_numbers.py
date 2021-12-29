____ typing _______ List, TypeVar
_______ math

T = TypeVar('T', int, float)


___ n_digit_number(number: T, n: int) -> int:
    '''converts number to an n-digit int, preserving sign'''
    sign = -1 __ number < 0 ____ 1
    num = abs(number)
    dexp = n - int(math.log10(num)) - 1 __ num !=0 ____ 0
    res = num * 10**(dexp)
    r.. int(sign * res)


___ n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    __ n < 1:
        raise ValueError
    r.. l..(map(l.... x: n_digit_number(x, n), numbers))
