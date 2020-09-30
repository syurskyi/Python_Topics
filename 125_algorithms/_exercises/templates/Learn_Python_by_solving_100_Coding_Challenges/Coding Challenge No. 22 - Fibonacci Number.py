# Fibonacci Sequence
# Question: Given a number as position of a Fibonacci number in the sequence, find its’ value
# Solutions:


class Solution:
    ___ fibR(self,n):
        __ n__1 or n__2:
            r_ 1
        r_ self.fibR(n-1)+ self.fibR(n-2)

Solution().fibR(6)