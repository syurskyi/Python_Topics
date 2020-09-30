# First Positive
# Question: Given an unsorted integer array, find the first missing positive integer.
# For example:
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# Solutions:


class Solution:
    # @param A, a list of integers
    # @return an integer
    # @a very subtle solution
    ___ firstMissingPositive(A):
        n=len(A)
        ___ i __ range(n):
            if A[i]<=0: A[i]=n+2
        ___ i __ range(n):
            if abs(A[i])<=n:
                curr=abs(A[i])-1
                A[curr]=-abs(A[curr])
        ___ i __ range(n):
            if A[i]>0: r_ i+1
        r_ n+1


Solution.firstMissingPositive([3,4,-1,1])