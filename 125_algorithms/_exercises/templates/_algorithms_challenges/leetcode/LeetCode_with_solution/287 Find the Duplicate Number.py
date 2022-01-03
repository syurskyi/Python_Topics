"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one
duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ findDuplicate(self, nums):
        """
        Condition for convert the array problem to linked list problem:
        CANNOT contains integer with 0; otherwise cycle: A = [1, 0]

        Degenerated case: if there is only one duplicates, just do arithmetic.

        For possibly multiple duplications: Floyd's loop detection
        Abstract the array to linked list, current index as value, current value as next
        Need to derive the math proof

        Abstract array to linked list
        :type nums: List[int]
        :rtype: int
        """
        f, s = 0, 0
        w... T...
            f = nums[nums[f]]
            s = nums[s]
            __ f __ s:
                break

        t = 0
        w.... t != s:
            t = nums[t]
            s = nums[s]

        r.. t


__ __name__ __ "__main__":
    ... Solution().findDuplicate([1, 2, 3 ,4, 5, 5]) __ 5

