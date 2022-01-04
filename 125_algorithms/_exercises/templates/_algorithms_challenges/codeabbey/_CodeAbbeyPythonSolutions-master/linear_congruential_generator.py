amount_values = i..(input())
results    # list

___ get_x_next(A,C,M,X0,N):
    __(N < 1):
        r.. X0
    x_next = (A*X0+C)%M
    r.. get_x_next(A,C,M, x_next, N-1)

___ i __ r..(amount_values):
    A,C,M,X0,N = map(i.., input().s..())
    results.a..(get_x_next(A,C,M,X0,N))

print(*results)
