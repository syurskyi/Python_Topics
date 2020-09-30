# Pow(x,n)
# Question: Implement pow(x, n).
# For Example: pow(3,2) returns 9
# Solutions:


class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    ___ pow_recursive(self, x, n):
        if n==0:
            r_ 1
        if n<0:
            r_ 1.0/self.pow_recursive(x,-n)
        if n%2==1:
            r_ x*self.pow_recursive(x*x,int(n/2))
        else:
            r_ self.pow_recursive(x*x,int(n/2))

    # @param x, a float
    # @param n, a integer
    # @return a float

    ___ pow_iterative(self, x, n):
        result=1
        if n<0:
            n=-n
            flag=1
        else:
            flag=0
        while n>0:
            if n%2==1:
                result=result*x
            x=x*x
            n/=2
        if flag==0:
            r_ result
        else:
            r_ 1.0/result


Solution().pow_recursive(3.0,2)