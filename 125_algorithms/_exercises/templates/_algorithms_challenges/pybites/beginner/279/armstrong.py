_______ math

___ is_armstrong(n: int) -> bool:
    # your code ...

    actual_num = n 

    digits = math.floor(math.log(n,10)) + 1

    print(digits)


    
    sum_digits =0

    while n:
        sum_digits += (n % 10)**digits
        n //= 10

    
    
    r.. sum_digits __ actual_num





