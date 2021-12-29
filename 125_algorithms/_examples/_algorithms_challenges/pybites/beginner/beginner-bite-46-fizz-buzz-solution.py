def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num