amount_values = int(input())
results = []

___ round(num1, num2):
    result = num1/num2
    is_negative = False
    __(result < 0):
        result = result * -1
        is_negative = True
    __(result + 0.5 >= int(result+1)):
        result = int(result + 1)
    else:
        result = int(result)
    
    __(is_negative):
        return result*-1
    return result

for i in range(amount_values):
    num1, num2 = map(int, input().split())
    results.append(round(num1,num2))
print(*results)