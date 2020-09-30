amount_values = int(input())
results =   # list

___ calc(A, B, C
    r_ A*B+C

___ sum_digits(num
    su. = 0
    w___(num != 0
        su. = su. + (num % 10)
        num //= 10
    r_ su.

___ i __ range(amount_values
    A, B, C = map(int, input().split())
    num = calc(A,B,C)
    results.append(sum_digits(num))

print(*results)

