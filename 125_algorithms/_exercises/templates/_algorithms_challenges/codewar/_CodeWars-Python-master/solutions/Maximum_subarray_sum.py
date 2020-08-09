"""
5 kyu: Maximum subarray sum
http://www.codewars.com/kata/maximum-subarray-sum/train/python

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


___ maxSequence(arr
    maximum = 0
    local_maximum = 0
    ___ i in arr:
        __ local_maximum > 0:
            local_maximum += i
            __ local_maximum < 0:
                local_maximum = 0
            ____ local_maximum > maximum:
                maximum = local_maximum
        ____ i > 0:
            local_maximum += i

    r_ maximum


assert maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) __ 6
