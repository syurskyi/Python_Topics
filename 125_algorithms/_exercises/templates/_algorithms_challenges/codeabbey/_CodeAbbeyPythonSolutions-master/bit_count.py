amount_values = i..(input
results    # list

___ c.. decimal_number
    is_negative = F..
    __(decimal_number < 0
        decimal_number *= -1
        decimal_number -=1
        is_negative = T..
    counter = 0
    w....(decimal_number != 0
        remainder = decimal_number%2
        __(remainder __ 1
            counter += 1
        decimal_number  //= 2

    __(is_negative
        r.. 32-counter
    r.. counter

values = l.. m..(i.., input().s..()))
___ i __ r..(amount_values
    results.a..(c.. values[i]

print(*results)