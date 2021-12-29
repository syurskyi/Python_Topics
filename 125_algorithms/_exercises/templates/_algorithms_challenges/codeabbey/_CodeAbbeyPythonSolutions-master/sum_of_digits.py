amount_values = int(input())
results = []

___ calc(A, B, C):
    return A*B+C

___ sum_digits(num):
    sum = 0
    while(num != 0):
        sum = sum + (num % 10)
        num //= 10
    return sum

for i in range(amount_values):
    A, B, C = map(int, input().split())
    num = calc(A,B,C)
    results.append(sum_digits(num))

print(*results)

