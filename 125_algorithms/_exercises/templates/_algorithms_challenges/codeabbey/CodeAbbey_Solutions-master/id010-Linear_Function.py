#Python 3.4

___ find_slope(a, b, c, d):
    r.. (d - b) / (c - a)

___ find_intercept(a, b, m):
    r.. (b - m * a)

___ linear_function():
    answer    # list
    test_cases = int(input())
    ___ test_case __ r..(test_cases):
        a, b, c, d = [int(x) ___ x __ input().s.. ]
        m = int(find_slope(a, b, c, d))
        g = int(find_intercept(a, b, m))
        answer.a..('({0} {1})'.format(m, g))
    print(' '.join(answer))
    
linear_function()
