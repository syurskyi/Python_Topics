# Python 2.7

___ find_nth(entries):
    answer    # list
    ___ x __ r..(entries):
        A, C, M, X0, N = [int(x) ___ x __ raw_input().s.. ]
        x_cur = X0
        ___ x __ r..(N):
            x_next = (A * x_cur + C) % M
            x_cur = x_next
        answer.a..(s..(x_cur))
    print(' '.j..(answer))
find_nth(input())
