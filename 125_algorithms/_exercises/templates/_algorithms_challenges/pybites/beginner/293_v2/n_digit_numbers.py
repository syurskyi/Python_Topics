____ typing _______ List, TypeVar
_______ math
T = TypeVar('T', i.., float)


___ n_digit_numbers(numbers: List[T], n: i..) __ List[i..]:

    __ n < 1:
        raise ValueError

    

    r.. [i..(number *10**(n -1)) __ number < 10**(n-1) ____ i..(number / 10**(math.floor(math.log(abs(number),10)) + 1 -n )) __ number > 10**(n -1) ____ i..(number) ___ number __ numbers]

