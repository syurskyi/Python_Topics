# Remove Element
# Question: Given an array and a value, remove all instances of that value in place and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory. The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example: Given input array nums = [3,2,2,3], val = 3
# Your function should return length = 2, with the first two elements of nums being 2.
# Solutions:


c_ Solution:
    # @param A a list of integers
    # @param elem an integer, value need to be removed
    # @return an integer
    ___ removeElement , A, elem:
        k _ 0
        ___ i __ A:
            __ i !_ elem:
                A[k] _ i
                k +_ 1
        r_ k


Solution .removeElement [1,2,4,3,3],3