amount_values = int(input())
results    # list

___ calc(A, B, C):
    r.. A*B+C

___ sum_digits(num):
    s.. = 0
    while(num != 0):
        s.. = s.. + (num % 10)
        num //= 10
    r.. s..

___ i __ r..(amount_values):
    A, B, C = map(int, input().split())
    num = calc(A,B,C)
    results.a..(sum_digits(num))

print(*results)

