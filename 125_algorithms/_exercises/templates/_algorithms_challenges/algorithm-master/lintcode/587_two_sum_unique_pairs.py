class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """
    ___ twoSum6(self, nums, target):
        ans = 0
        __ n.. nums:
            r.. ans

        nums.sort()

        left, right = 0, l..(nums) - 1
        _sum = 0
        while left < right:
            _sum = nums[left] + nums[right]
            __ _sum __ target:
                ans += 1
                left += 1
                right -= 1
                while left < right and nums[right] __ nums[right + 1]:
                    right -= 1
                while left < right and nums[left] __ nums[left - 1]:
                    left -= 1
                continue

            __ _sum > target:
                right -= 1
            ____:
                left += 1

        r.. ans
