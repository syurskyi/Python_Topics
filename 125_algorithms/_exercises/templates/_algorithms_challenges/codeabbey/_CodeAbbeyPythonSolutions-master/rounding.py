amount_values = int(input())
results    # list

___ round(num1, num2):
    result = num1/num2
    is_negative = F..
    __(result < 0):
        result = result * -1
        is_negative = T..
    __(result + 0.5 >= int(result+1)):
        result = int(result + 1)
    ____:
        result = int(result)
    
    __(is_negative):
        r.. result*-1
    r.. result

___ i __ r..(amount_values):
    num1, num2 = map(int, input().s..())
    results.a..(round(num1,num2))
print(*results)