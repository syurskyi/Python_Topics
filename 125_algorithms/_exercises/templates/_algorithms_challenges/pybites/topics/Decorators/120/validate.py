____ f.. _______ wraps


___ int_args(func
    $w.. f..
    # complete this decorator
    ___ wrapper $
        __ s..(isi..(n, s..) ___ n __ args
            r.. T..
        ____ s..(isi..(n, f__) ___ n __ args
            r.. T..
        ____ s..(n < 0 ___ n __ args
            r.. V...
        ____ a..(isi..(n, i..) ___ n __ args
            r.. func $)
    r.. wrapper
""" 
@int_args
def sum_numbers(*numbers):
    return sum(numbers)

print(sum_numbers(1, 'string', 3)) """