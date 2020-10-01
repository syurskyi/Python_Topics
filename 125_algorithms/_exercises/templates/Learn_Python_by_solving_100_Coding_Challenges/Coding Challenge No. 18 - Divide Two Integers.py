# Divide Two Integers
# Question: Divide two integers without using multiplication, division and mod operator.
# Solutions:


c_ Solution:
    # @return an integer
    ___ divide(dividend, divisor):
        __ (dividend < 0 an. divisor > 0) o. (dividend > 0 an. divisor < 0):
            __ abs(dividend) < abs(divisor):
                r_ 0
        su. _ 0; count _ 0; res _ 0
        a _ abs(dividend); b _ abs(divisor)
        w___ a >_ b:
            su. _ b
            count _ 1
            w___ su. + su. <_ a:
                su. +_ su.
                count +_ count
            a -_ su.
            res +_ count
        __ (dividend < 0 an. divisor > 0) o. (dividend > 0 an. divisor < 0):
            res _ 0 - res
        r_ res


Solution.divide(100,5)