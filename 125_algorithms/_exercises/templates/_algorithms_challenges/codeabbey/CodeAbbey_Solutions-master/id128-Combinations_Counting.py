# Python 2.7
___ factorial_of(number):
    ans = 1
    ___ x __ r..(1,number+1):
        ans *= x
    r.. ans

___ combinations_counting(test_cases):
    answer    # list
    ___ x __ r..(test_cases):
        n, k = [int(x) ___ x __ raw_input().s.. ]
        case_answer = factorial_of(n) / (factorial_of(k) * factorial_of(n - k))
        answer.a..(s..(case_answer))
    print(' '.join(answer))
        
combinations_counting(input())
