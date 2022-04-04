____ t___ _______ L.., TypeVar
T = TypeVar('T', i.., f__)


___ n_digit_numbers(numbers: L..[T], n: i..) __ L..[i..]:
    number_list    # list
    __ n __ 0:
        r.. V...
    ___ number __ numbers:
        __ number __ 0:
            number_list.a..(0)
        number_of_digits = l..(s..(number).r..('.', ''
        __ number >= 1:
            __ number_of_digits <= n:
                number_list.a..(i..(s..(number * 10 **n)[:n]
            ____ number_of_digits >= n:
                number_list.a..(i..(s..(number * 10 **n)[:n]
        __ number <= -1:
            __ number_of_digits <= n:
                number_list.a..(i..(s..(number * 10 **n)[:n + 1]
            ____ number_of_digits > n:
                number_list.a..(i..(s..(number * 10 **n)[:n + 1]
            ____
                number_list.a..(number)
    r.. number_list