class Solution:
    """
    @param: nums: an array of integer
    @param: target: an integer
    @return: an integer
    """
    ___ twoSum5(self, nums, target
        ans = 0

        __ not nums or le.(nums) < 2:
            r_ ans

        nums.sort()

        left, right = 0, le.(nums) - 1
        w___ left < right:
            __ nums[left] + nums[right] <= target:
                # the count of connections from `left` to `right`
                # e.g, from 1 to 4, 1-2, 1-3, 1-4, got 3 connections
                ans += right - left
                left += 1
            ____
                right -= 1

        r_ ans
