# Swap Two Variables
# Question: swap two variables without using a third.
# Solutions:


class Solution:
    def swap1(self,x,y):
        x,y = y,x
        return x,y

    def swap2(self,x,y):
        x = x + y
        y = x - y
        x = x - y
        return x,y

    def swap3(self,x,y):
        x = x * y
        y = int(x / y)
        x = int(x / y)
        return x,y

    def swap4(self,x,y):
        x = x ^ y
        y = x ^ y
        x = x ^ y
        return x,y

print ( Solution().swap1(9,6) )
print ( Solution().swap2(9,6) )
print ( Solution().swap3(9,6) )
print ( Solution().swap4(9,6) )