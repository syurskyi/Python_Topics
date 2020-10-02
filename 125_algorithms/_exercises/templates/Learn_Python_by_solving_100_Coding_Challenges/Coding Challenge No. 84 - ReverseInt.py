# Reverse Integer
# Question: Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321.
# Solutions:


c_ Solution:
    # @return an integer
    ___ reverse , x:
        __ x<0:
            sign _ -1
        ____
            sign _ 1
        strx_str ab. x
        r _ strx[::-1]
        r_ sign*in. r


Solution .reverse 123