amount_values i..(input
results    # list

___ r..(num1, num2
    result num1/num2
    is_negative F..
    __(result < 0
        result result * -1
        is_negative T..
    __(result + 0.5 >_ i..(result+1:
        result i..(result + 1)
    ____
        result i..(result)
    
    __(is_negative
        r.. ?*-1
    r.. ?

___ i __ r..(amount_values
    num1, num2 m.. i.., i.. ).s..
    results.a..(r..(num1,num2
print(*results)