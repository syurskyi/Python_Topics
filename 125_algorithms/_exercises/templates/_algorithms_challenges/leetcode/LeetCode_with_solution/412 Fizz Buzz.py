"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output "Fizz" instead of the number and for the multiples of five output "Buzz".
For numbers which are multiples of both three and five output "FizzBuzz".

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
__author__ = 'Daniel'


class Solution(object):
    ___ fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret    # list
        ___ i __ xrange(1, n+1):
            cur = ""
            __ i % 3 __ 0:
                cur += "Fizz"
            __ i % 5 __ 0:
                cur += "Buzz"
            __ n.. cur:
                cur = str(i)

            ret.a..(cur)

        r.. ret