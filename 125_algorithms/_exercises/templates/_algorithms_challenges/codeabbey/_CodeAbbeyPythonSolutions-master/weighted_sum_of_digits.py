amount_values i..(input
results    # list

___ get_weight(num
    len_of_num l..(s..(num
    weight_sum 0
    ___ i __ r..(len_of_num, 0, -1
        weight_sum += num%10*i
        num //= 10
    results.a..(weight_sum)

values l.. m..(i.., i.. ).s..()))
___ i __ r..(amount_values
    get_weight(values[i])

print(*results)
