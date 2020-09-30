# Fibonacci Sequence
# Question: Given a number as position of a Fibonacci number in the sequence, find its’ value
# Solutions:


class Solution:
    def fibR(self,n):
        if n==1 or n==2:
            return 1
        return self.fibR(n-1)+ self.fibR(n-2)

Solution().fibR(6)