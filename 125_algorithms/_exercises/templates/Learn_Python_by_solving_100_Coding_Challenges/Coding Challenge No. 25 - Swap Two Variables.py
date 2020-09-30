# Swap Two Variables
# Question: swap two variables without using a third.
# Solutions:


class Solution:
    ___ swap1(self,x,y):
        x,y = y,x
        r_ x,y

    ___ swap2(self,x,y):
        x = x + y
        y = x - y
        x = x - y
        r_ x,y

    ___ swap3(self,x,y):
        x = x * y
        y = int(x / y)
        x = int(x / y)
        r_ x,y

    ___ swap4(self,x,y):
        x = x ^ y
        y = x ^ y
        x = x ^ y
        r_ x,y

print ( Solution().swap1(9,6) )
print ( Solution().swap2(9,6) )
print ( Solution().swap3(9,6) )
print ( Solution().swap4(9,6) )