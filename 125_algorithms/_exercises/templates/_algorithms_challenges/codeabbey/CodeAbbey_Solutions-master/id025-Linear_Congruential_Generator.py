# Python 2.7

___ find_nth(entries
    answer =   # list
    ___ x __ range(entries
        A, C, M, X0, N = [int(x) ___ x __ raw_input().split()]
        x_cur = X0
        ___ x __ range(N
            x_next = (A * x_cur + C) % M
            x_cur = x_next
        answer.append(str(x_cur))
    print(' '.join(answer))
find_nth(input())
