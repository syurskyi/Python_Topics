amount_value = int(input())

generator_list = []
results = []

___ generate(num, counter
    
    __(num in generator_list
        r_ counter
    generator_list.append(num)
    num **= 2
    num = (num//100)%10000
    r_ generate(num, counter+1)

values = list(map(int, input().split()))

___ i in range(amount_value
    results.append(generate(values[i],0))
    generator_list.clear()

print(*results)