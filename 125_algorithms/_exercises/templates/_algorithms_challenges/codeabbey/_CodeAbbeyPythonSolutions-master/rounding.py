amount_values = i..(input())
results    # list

___ r..(num1, num2
    result = num1/num2
    is_negative = F..
    __(result < 0
        result = result * -1
        is_negative = T..
    __(result + 0.5 >= i..(result+1)):
        result = i..(result + 1)
    ____:
        result = i..(result)
    
    __(is_negative
        r.. result*-1
    r.. result

___ i __ r..(amount_values
    num1, num2 = map(i.., input().s..())
    results.a..(r..(num1,num2))
print(*results)