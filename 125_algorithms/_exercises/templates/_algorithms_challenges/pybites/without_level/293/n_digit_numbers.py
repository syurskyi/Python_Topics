____ typing _______ List, TypeVar
_______ math

T = TypeVar('T', i.., float)


___ n_digit_number(number: T, n: i..) __ i..:
    '''converts number to an n-digit int, preserving sign'''
    sign = -1 __ number < 0 ____ 1
    num = abs(number)
    dexp = n - i..(math.log10(num)) - 1 __ num !=0 ____ 0
    res = num * 10**(dexp)
    r.. i..(sign * res)


___ n_digit_numbers(numbers: List[T], n: i..) __ List[i..]:
    __ n < 1:
        r.. ValueError
    r.. l..(map(l.... x: n_digit_number(x, n), numbers))
