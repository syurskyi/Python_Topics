class Solution:
    """
    @param: nums: an array of integer
    @param: target: an integer
    @return: an integer
    """
    ___ twoSum5(self, nums, target):
        ans = 0

        __ n.. nums o. l..(nums) < 2:
            r.. ans

        nums.s..()

        left, right = 0, l..(nums) - 1
        w.... left < right:
            __ nums[left] + nums[right] <= target:
                # the count of connections from `left` to `right`
                # e.g, from 1 to 4, 1-2, 1-3, 1-4, got 3 connections
                ans += right - left
                left += 1
            ____:
                right -= 1

        r.. ans
