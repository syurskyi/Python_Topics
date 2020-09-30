'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object
    ___ fizzBuzz(self, n
        result =   # list
        ___ num __ range(1, n+1
            __ num % 15 __ 0:
                result.append('FizzBuzz')
            ____ num % 5 __ 0:
                result.append('Buzz')
            ____ num % 3 __ 0:
                result.append('Fizz')
            ____
                result.append(str(num))
        r_ result
