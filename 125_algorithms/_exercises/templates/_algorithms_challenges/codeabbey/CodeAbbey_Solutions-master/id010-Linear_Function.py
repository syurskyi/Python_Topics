#Python 3.4

___ find_slope(a, b, c, d
    r_ (d - b) / (c - a)

___ find_intercept(a, b, m
    r_ (b - m * a)

___ linear_function(
    answer = []
    test_cases = int(input())
    ___ test_case in range(test_cases
        a, b, c, d = [int(x) ___ x in input().split()]
        m = int(find_slope(a, b, c, d))
        g = int(find_intercept(a, b, m))
        answer.append('({0} {1})'.format(m, g))
    print(' '.join(answer))
    
linear_function()
