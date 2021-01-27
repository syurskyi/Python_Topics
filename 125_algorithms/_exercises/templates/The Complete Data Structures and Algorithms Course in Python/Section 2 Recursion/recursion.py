#### Russian Doll recursive function ###

___ openRussianDoll(doll
    __ doll == 1:
        print("All dolls are opened")
    ____
        openRussianDoll(doll-1)


openRussianDoll(4)


# ___ recursionMethod(parameters):
#     if  exit from condition satisfied:
#         return some value
#     else:
#         recursionMethod(modified parameters)


___ firstMethod(
    secondMethod()
    print("I am the first Method")

___ secondMethod(
    thirdMethod()
    print("I am the second Method")

___ thirdMethod(
    fourthMethod()
    print("I am the third Method")

___ fourthMethod(
    print("I am the fourth Method")


firstMethod()


___ recursiveMethod(n
    __ n<1:
        print("n is less than 1")
    ____
        recursiveMethod(n-1)
        print(n)

recursiveMethod(4)
 ## Recursion vs Iterarion###

___ powerOfTwo(n
    __ n == 0:
         return 1
    ____
        power = powerOfTwo(n-1)
        return power * 2

print(powerOfTwo(3))

___ powerOfTwoIt(n
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power


print(powerOfTwoIt(4))

 ## Factorial###


___ factorial(n
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    __ n in [0,1]:
        return 1
    ____
        return n * factorial(n-1)


 ## Fibonacci###

___ fibonacci(n
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer.'
    __ n in [0,1]:
        return n
    ____
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))
