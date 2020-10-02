# Jump Game
# Question: Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# For example:
# A = [2,3,1,1,4], return true.
# A = [3,2,1,0,4], return false.
# Solutions:


c_ Solution:
    # @param A, a list of integers
    # @return a boolean
    ___ canJump , A:
        step _ A[0]
        ___ i __ ra.. 1, le. A:
            __ step > 0:
                step -_ 1
                step _ ma. step, A[i]
        ____
            r_ F..
        r_ T..


Solution .canJump [3,2,1,0,4]