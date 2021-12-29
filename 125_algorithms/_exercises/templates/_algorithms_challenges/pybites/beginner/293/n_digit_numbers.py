____ typing _______ List, TypeVar
T = TypeVar('T', int, float)


___ n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    new_numbers    # list
    __ n >= 1:
        ___ number __ numbers:
            new_number = str(number).replace('.','')
            __ new_number[0] __ '-':
                new_number = new_number[:n+1]
            ____:
                new_number = new_number[:n]
            new_numbers.a..(int(new_number))
        print(new_numbers)
        r.. [number*(10**(n-l..(str(number))))
                __ number > 0 ____ number*(10**(n-l..(str(number).replace('-',''))))
                ___ number __ new_numbers]
    ____:
        raise ValueError


number = 12.34
temp_number = str(number).replace('.','')[:3]
print(temp_number)

#print(n_digit_numbers([1.1, 2, -3], 2))