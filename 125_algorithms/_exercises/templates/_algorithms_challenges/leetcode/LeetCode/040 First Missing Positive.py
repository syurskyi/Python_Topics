"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
__author__ = 'Danyang'
class Solution:
    ___ firstMissingPositive(self, A
        """
        Bucket Sort without extra space
        O(n)

        Extra space is eliminated by using the array A itself as a storage

        :param A: a list of integers
        :return: an integer
        """
        __ not A:
            r_ 1

        i = 0
        length = le.(A)
        w___ i<length:
            current = A[i]
            __ current<=0 or current>length or A[current-1]__current:  # out-of-range or in-place
                i += 1
            ____
                A[current-1], A[i] = current, A[current-1]   # go to the next iteration


        ___ i in xrange(length
            __ A[i]!=i+1:
                r_ i+1
        r_ A[-1]+1


__ __name____"__main__":
    assert Solution().firstMissingPositive([3,4,-1,1])__2