"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
__author__ = 'Danyang'
c_ Solution:
    ___ firstMissingPositive  A):
        """
        Bucket Sort without extra space
        O(n)

        Extra space is eliminated by using the array A itself as a storage

        :param A: a list of integers
        :return: an integer
        """
        __ n.. A:
            r.. 1

        i = 0
        length = l..(A)
        w.... i<length:
            current = A[i]
            __ current<=0 o. current>length o. A[current-1]__current:  # out-of-range or in-place
                i += 1
            ____:
                A[current-1], A[i] = current, A[current-1]   # go to the next iteration


        ___ i __ xrange(length):
            __ A[i]!=i+1:
                r.. i+1
        r.. A[-1]+1


__ _____ __ ____
    ... Solution().firstMissingPositive([3,4,-1,1])__2