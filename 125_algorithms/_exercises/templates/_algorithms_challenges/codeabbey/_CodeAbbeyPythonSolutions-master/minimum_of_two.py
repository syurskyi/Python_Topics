amount_values i..(input
results    # list

___ get_min(num1, num2
    m.. 0
    __(num1 < num2
        m.. num1
    ____
        m.. num2

    r.. m..

___ i __ r..(amount_values
    num1, num2 map(i.., input().s..
    results.a..(get_min(num1, num2

print(*results)