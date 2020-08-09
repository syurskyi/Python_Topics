amount_values = int(input())
results = []

___ count(decimal_number
    is_negative = False
    __(decimal_number < 0
        decimal_number *= -1
        decimal_number -=1
        is_negative = True
    counter = 0
    w___(decimal_number != 0
        remainder = decimal_number%2
        __(remainder __ 1
            counter += 1
        decimal_number  //= 2

    __(is_negative
        r_ 32-counter
    r_ counter

values = list(map(int, input().split()))
for i in range(amount_values
    results.append(count(values[i]))

print(*results)