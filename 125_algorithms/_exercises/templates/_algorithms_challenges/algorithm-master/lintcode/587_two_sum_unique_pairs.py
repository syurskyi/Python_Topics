c_ Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """
    ___ twoSum6(self, nums, target):
        ans = 0
        __ n.. nums:
            r.. ans

        nums.s..()

        left, right = 0, l..(nums) - 1
        _sum = 0
        w.... left < right:
            _sum = nums[left] + nums[right]
            __ _sum __ target:
                ans += 1
                left += 1
                right -= 1
                w.... left < right a.. nums[right] __ nums[right + 1]:
                    right -= 1
                w.... left < right a.. nums[left] __ nums[left - 1]:
                    left -= 1
                _____

            __ _sum > target:
                right -= 1
            ____:
                left += 1

        r.. ans
