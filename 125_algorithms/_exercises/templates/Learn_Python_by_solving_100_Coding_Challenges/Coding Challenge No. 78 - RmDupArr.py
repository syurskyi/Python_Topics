# Remove Duplicates from Sorted Array
# Question: Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# For example: Given input array nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
# Solutions:


class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    ___ removeDuplicates(self, A):
        # write your code here
        if A ==   # list:
            r_ 0
        count = 0
        ___ i __ range(0, len(A)):
            if A[i] == A[i-1]:
                continue
            else:
                A[count] = A[i]
                count += 1
        r_ count


Solution().removeDuplicates([1,1,2])