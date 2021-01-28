#### Russian Doll recursive function ###

def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)


openRussianDoll(4)


# ___ recursionMethod(parameters):
#     if  exit from condition satisfied:
#         return some value
#     else:
#         recursionMethod(modified parameters)


def firstMethod():
    secondMethod()
    print("I am the first Method")

def secondMethod():
    thirdMethod()
    print("I am the second Method")

def thirdMethod():
    fourthMethod()
    print("I am the third Method")

def fourthMethod():
    print("I am the fourth Method")


firstMethod()


def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

recursiveMethod(4)


 ## Recursion vs Iterarion###

def powerOfTwo(n):
    if n == 0:
         return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

print(powerOfTwo(3))

def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power


print(powerOfTwoIt(4))

#  ## Factorial###
#
#
# ___ factorial n
#     a__ ? >_ 0 a__ in. ? __ ? 'The number must be positive integer only!'
#     __ ? __  0,1
#         r_ 1
#     ____
#         r_ ? * ? ?- 1
#
#
#  ## Fibonacci###
#
# ___ fibonacci n
#     a__ ? >_0 a__ in. ? __ ? 'Fibonacci number cannot be negative number or non integer.'
#     __ ? __ 0,1
#         r_ ?
#     ____
#         r_ ? ? - 1 + ? ? - 2
#
# print ?7
