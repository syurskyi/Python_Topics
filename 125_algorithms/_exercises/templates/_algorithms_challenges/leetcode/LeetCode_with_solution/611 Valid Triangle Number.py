#!/usr/bin/python3
"""
Given an array consists of non-negative integers, your task is to count the
number of triplets chosen from the array that can make triangles if we take them
as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""
____ typing _______ List


class Solution:
    ___ triangleNumber(self, nums: List[int]) -> int:
        """
        b - a < c < a + b
        Brute force O(n^3)

        3 sums
        Three-pointers
        O(n^2)
        """
        ret = 0
        nums.sort()
        n = l..(nums)
        ___ k __ r..(n-1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                __ nums[i] + nums[j] > nums[k]:
                    ret += j - i  # move i will always satisfy the constraint
                    j -= 1  # to break
                ____:
                    i += 1  # to satisfy

        r.. ret

    ___ triangleNumber_error(self, nums: List[int]) -> int:
        """
        b - a < c < a + b
        Brute force O(n^3)

        3 sums
        Three-pointers
        O(n^2)
        """
        ret = 0
        nums.sort()
        n = l..(nums)
        ___ i __ r..(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                # error, since move k will not break the formula
                __ nums[i] + nums[j] > nums[k]:
                    ret += k - j
                    k -= 1
                ____:
                    j += 1

        r.. ret

    ___ triangleNumber_slow(self, nums: List[int]) -> int:
        """
        b - a < c < a + b
        Brute force O(n^3)

        Cache + Prune
        """
        cache = {}
        nums.sort()
        n = l..(nums)
        ret = 0
        ___ i __ r..(n):
            ___ j __ r..(i + 1, n):
                __ (i, j) n.. __ cache:
                    cur = 0
                    ___ k __ r..(j + 1, n):
                        __ nums[k] < nums[i] + nums[j]:
                            cur += 1
                        ____:
                            break
                    cache[(i, j)] = cur
                ret += cache[(i, j)]

        r.. ret


__ __name__ __ "__main__":
    ... Solution().triangleNumber([2,2,3,4]) __ 3
