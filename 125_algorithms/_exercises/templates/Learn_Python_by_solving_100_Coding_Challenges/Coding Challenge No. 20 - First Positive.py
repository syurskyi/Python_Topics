# First Positive
# Question: Given an unsorted integer array, find the first missing positive integer.
# For example:
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# Solutions:


c_ Solution:
    # @param A, a list of integers
    # @return an integer
    # @a very subtle solution
    ___ firstMissingPositive(A):
        n_len(A)
        ___ i __ ra..(n):
            __ A[i]<_0: A[i]_n+2
        ___ i __ ra..(n):
            __ abs(A[i])<_n:
                curr_abs(A[i])-1
                A[curr]_-abs(A[curr])
        ___ i __ ra..(n):
            __ A[i]>0: r_ i+1
        r_ n+1


Solution.firstMissingPositive([3,4,-1,1])