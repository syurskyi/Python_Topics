class Solution:
    """
    @param: nums: an integer array
    @param: target: An integer
    @return: the difference between the sum and the target
    """
    ___ twoSumClosest(self, nums, target
        __ not nums or le.(nums) < 2:
            r_ -1

        nums.sort()

        left, right = 0, le.(nums) - 1
        _sum = 0
        diff = float('inf')
        w___ left < right:
            _sum = nums[left] + nums[right]
            __ _sum < target:
                diff = min(diff, target - _sum)
                left += 1
            ____
                diff = min(diff, _sum - target)
                right -= 1

        r_ diff
