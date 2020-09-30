# Remove Element
# Question: Given an array and a value, remove all instances of that value in place and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory. The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example: Given input array nums = [3,2,2,3], val = 3
# Your function should return length = 2, with the first two elements of nums being 2.
# Solutions:


class Solution:
    # @param A a list of integers
    # @param elem an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        k = 0
        for i in A:
            if i != elem:
                A[k] = i
                k += 1
        return k


Solution().removeElement([1,2,4,3,3],3)