#!/usr/bin/python3
"""
Given a non-negative integer, you could swap two digits at most once to get the
maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""


class Solution:
    ___ maximumSwap(self, num: int) -> int:
        """
        stk maintain a increasing stack from right to left
        """
        stk    # list
        nums = l..(str(num))
        n = l..(nums)
        ___ i __ r..(n-1, -1, -1):
            __ stk and stk[-1][1] >= nums[i]:  # only keep the rightmost duplicate
                continue
            stk.a..((i, nums[i]))

        ___ i __ r..(n):
            while stk and stk[-1][0] <= i:
                stk.pop()
            __ stk and stk[-1][1] > nums[i]:
                j = stk[-1][0]
                nums[i], nums[j] = nums[j], nums[i]
                break

        r.. int("".join(nums))


__ __name__ __ "__main__":
    ... Solution().maximumSwap(2736) __ 7236
    ... Solution().maximumSwap(9973) __ 9973
