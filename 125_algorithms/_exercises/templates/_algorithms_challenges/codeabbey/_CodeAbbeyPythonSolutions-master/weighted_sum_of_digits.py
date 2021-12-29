amount_values = int(input())
results    # list

___ get_weight(num):
    len_of_num = l..(str(num))
    weight_sum = 0
    ___ i __ r..(len_of_num, 0, -1):
        weight_sum += num%10*i
        num //= 10
    results.a..(weight_sum)

values = l..(map(int, input().split()))
___ i __ r..(amount_values):
    get_weight(values[i])

print(*results)
