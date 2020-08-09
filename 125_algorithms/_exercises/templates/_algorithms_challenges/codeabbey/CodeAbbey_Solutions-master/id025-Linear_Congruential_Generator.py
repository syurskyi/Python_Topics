# Python 2.7

___ find_nth(entries
    answer = []
    ___ x in range(entries
        A, C, M, X0, N = [int(x) ___ x in raw_input().split()]
        x_cur = X0
        ___ x in range(N
            x_next = (A * x_cur + C) % M
            x_cur = x_next
        answer.append(str(x_cur))
    print(' '.join(answer))
find_nth(input())
