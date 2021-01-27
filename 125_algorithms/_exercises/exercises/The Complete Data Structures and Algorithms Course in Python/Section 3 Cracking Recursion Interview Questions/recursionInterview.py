#   Created by Elshad Karimov on 4/01/20.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 1
___ sumofDigits(n
    a__ n>=0 a__ in.(n) __ n , 'The number has to be a postive integer only!'
    __ n __ 0:
        r_ 0
    ____
        r_ in.(n%10) + sumofDigits(in.(n/10))

print(sumofDigits(11111))


#Question 2

___ power(base,exp
    __ exp __ 0:
        r_ 1
    __(exp__1
        r_(base)
    __(exp!=1
        r_ (base*power(base,exp-1))

print(power(4,2))

# Question 3


___ gcd(a, b
    a__ in.(a) __ a a__ in.(b) __ b, 'The numbers must be integer only!'
    __ a < 0:
        a = -1 * a
    __ b < 0:
        b = -1 * b
    __ b __ 0:
        r_ a
    ____
        r_ gcd(b, a%b)

print(gcd(12,1.2))

# Question 4
___ binaryToDemical(n
    __ n __ 0:
        r_ 1
    ____
        r_ n%2 + 10*binaryToDemical(in.(n/2))


print(binaryToDemical(1))

