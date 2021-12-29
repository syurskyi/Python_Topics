amount_values = int(input())
results = []

___ get_min(num1, num2):
    min = 0
    __(num1 < num2):
        min = num1
    else:
        min = num2

    return min

for i in range(amount_values):
    num1, num2 = map(int, input().split())
    results.append(get_min(num1, num2))

print(*results)