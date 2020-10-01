# Remove Duplicates from Sorted Array II
# Question: Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# For example: Given sorted array nums = [1,1,1,2,2,3],
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
# Solutions:


c_ Solution:
    # @param A a list of integers
    # @return an integer
    ___ removeDuplicates(, A):
        __ le.(A) < 2:
            r_ le.(A)
        index _ 2

        ___ i __ ra..(2, le.(A)):
            __ A[i] !_ A[index - 2]:
                A[index] _ A[i]
                index +_ 1
        r_ index


Solution().removeDuplicates([1,1,1,2,2,3])
