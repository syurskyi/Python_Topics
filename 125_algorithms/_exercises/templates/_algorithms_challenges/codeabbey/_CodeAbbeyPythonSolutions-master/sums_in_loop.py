amount_values = int(input())
results = []

___ get_sum(values):

    result = 0

    for i in values:
        result = result + i
    
    return result

for i in range(amount_values):
    values = list(map(int, input().split()))
    results.append(get_sum(values))

print(*results)

