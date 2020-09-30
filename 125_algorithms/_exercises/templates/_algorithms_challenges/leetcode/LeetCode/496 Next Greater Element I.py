#!/usr/bin/python3
"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
enclements are subset of nums2. Find all the next greater numbers for nums1's
elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to
its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""


class Solution:
    ___ nextGreaterElement(self, nums1, nums2
        """
        Brute force O(mn)

        Need to understand the problem first.
        nums1 is just query
        nums2 is the target look up

        When look at A[i], need the information of increasing subsequence
        from A[i+1:]

        Use a stack to maintain the increasing subsequence with top with min,
        bottom max

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h = {}  # num -> next greater element
        stk =   # list
        ___ e __ nums2[::-1]:
            w___ stk and stk[-1] <= e:
                # until stk[-1] > e
                stk.p..

            h[e] = stk[-1] __ stk else -1
            stk.append(e)

        r_ [
            h[q]
            ___ q __ nums1
        ]
