# Pow(x,n)
# Question: Implement pow(x, n).
# For Example: pow(3,2) returns 9
# Solutions:


c_ Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    ___ pow_recursive , x, n:
        __ n__0:
            r_ 1
        __ n<0:
            r_ 1.0/pow_recursive x,-n
        __ n%2__1:
            r_ x*pow_recursive x*x,in. n/2
        ____
            r_ pow_recursive x*x,in. n/2

    # @param x, a float
    # @param n, a integer
    # @return a float

    ___ pow_iterative , x, n:
        result_1
        __ n<0:
            n_-n
            flag_1
        ____
            flag_0
        w___ n>0:
            __ n%2__1:
                result_result*x
            x_x*x
            n/_2
        __ flag__0:
            r_ result
        ____
            r_ 1.0/result


Solution .pow_recursive 3.0,2