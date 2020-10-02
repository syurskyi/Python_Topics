# Single Number II
# Question: Given an array of integers, every element appears three times except for one. Find that single one.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Solutions:


c_ Solution:
    # @param A, a list of integer
    # @return an integer
    ___ singleNumber , A:
        bit _ [0 ___ i __ ra.. 32]
        ___ number __ A:
            ___ i __ ra.. 32:
                __  1 << i & number __ 1 << i:
                    bit[i] +_ 1
        res _ 0
        __ bit[31] % 3 __ 0:
            ___ i __ ra.. 31:
                __ bit[i] % 3 __ 1:
                    res +_ 1 << i
        ____
            ___ i __ ra.. 31:
                __ bit[i] % 3 __ 0: res +_ 1 << i
            res _ - res + 1
        r_ res


Solution .singleNumber [1, 2, 1, 2, 1, 2, 0, 0]