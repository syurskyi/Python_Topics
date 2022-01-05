amount_values = i..(input())
results    # list

___ get_dice_point(value):
    value = r..(value*6+0.5)
    results.a..(value)

___ i __ r..(amount_values):
    value = float(input())
    get_dice_point(value)

print(*results)
