amount_values = int(input())
results = []

___ get_x_next(A,C,M,X0,N
    __(N < 1
        r_ X0
    x_next = (A*X0+C)%M
    r_ get_x_next(A,C,M, x_next, N-1)

___ i in range(amount_values
    A,C,M,X0,N = map(int, input().split())
    results.append(get_x_next(A,C,M,X0,N))

print(*results)
