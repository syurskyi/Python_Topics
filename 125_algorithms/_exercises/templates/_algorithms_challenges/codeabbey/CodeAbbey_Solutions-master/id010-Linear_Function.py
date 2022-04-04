#Python 3.4

___ find_slope(a, b, c, d
    r.. (d - b) / (c - a)

___ find_intercept(a, b, m
    r.. (b - m * a)

___ linear_function
    answer    # list
    test_cases  i..(input
    ___ test_case __ r..(test_cases
        a, b, c, d  [i..(x) ___ x __ input().s.. ]
        m  i..(find_slope(a, b, c, d
        g  i..(find_intercept(a, b, m
        answer.a..('({0} {1})'.f..(m, g
    print(' '.j..(answer
    
linear_function()
