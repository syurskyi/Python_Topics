___ fizzbuzz(num):
    __ num % 3 __ 0 and num % 5 __ 0:
        r.. "Fizz Buzz"
    ____ num % 3 __ 0:
        r.. "Fizz"
    ____ num % 5 __ 0:
        r.. "Buzz"
    ____:
        r.. num

___ i __ r..(34):
    print(i, fizzbuzz(i))