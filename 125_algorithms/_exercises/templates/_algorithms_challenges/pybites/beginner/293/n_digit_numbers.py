____ t___ _______ L.., TypeVar
T = TypeVar('T', i.., f__)


___ n_digit_numbers(numbers: L..[T], n: i..) __ L..[i..]:
    new_numbers    # list
    __ n >= 1:
        ___ number __ numbers:
            new_number = s..(number).r..('.','')
            __ new_number[0] __ '-':
                new_number = new_number[:n+1]
            ____:
                new_number = new_number[:n]
            new_numbers.a..(i..(new_number
        print(new_numbers)
        r.. [number*(10**(n-l..(s..(number))))
                __ number > 0 ____ number*(10**(n-l..(s..(number).r..('-',''))))
                ___ number __ new_numbers]
    ____:
        r.. V...


number = 12.34
temp_number = s..(number).r..('.','')[:3]
print(temp_number)

#print(n_digit_numbers([1.1, 2, -3], 2))