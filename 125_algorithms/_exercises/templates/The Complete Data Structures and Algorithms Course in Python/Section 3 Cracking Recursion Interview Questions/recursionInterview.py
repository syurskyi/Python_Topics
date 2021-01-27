#   Created by Elshad Karimov on 4/01/20.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 1
___ sumofDigits(n
    assert n>=0 and int(n) == n , 'The number has to be a postive integer only!'
    __ n == 0:
        return 0
    ____
        return int(n%10) + sumofDigits(int(n/10))

print(sumofDigits(11111))


#Question 2

___ power(base,exp
    __ exp == 0:
        return 1
    __(exp==1
        return(base)
    __(exp!=1
        return (base*power(base,exp-1))

print(power(4,2))

# Question 3


___ gcd(a, b
    assert int(a) == a and int(b) == b, 'The numbers must be integer only!'
    __ a < 0:
        a = -1 * a
    __ b < 0:
        b = -1 * b
    __ b == 0:
        return a
    ____
        return gcd(b, a%b)

print(gcd(12,1.2))

# Question 4
___ binaryToDemical(n
    __ n == 0:
        return 1
    ____
        return n%2 + 10*binaryToDemical(int(n/2))


print(binaryToDemical(1))

