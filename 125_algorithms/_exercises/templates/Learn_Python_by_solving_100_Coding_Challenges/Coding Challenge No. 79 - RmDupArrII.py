# Remove Duplicates from Sorted Array II
# Question: Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# For example: Given sorted array nums = [1,1,1,2,2,3],
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
# Solutions:


class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2:
            return len(A)
        index = 2

        for i in range(2, len(A)):
            if A[i] != A[index - 2]:
                A[index] = A[i]
                index += 1
        return index


Solution().removeDuplicates([1,1,1,2,2,3])
