c_ Solution:
    """
    @param: nums: an integer array
    @param: target: An integer
    @return: the difference between the sum and the target
    """
    ___ twoSumClosest(self, nums, target):
        __ n.. nums o. l..(nums) < 2:
            r.. -1

        nums.s..()

        left, right = 0, l..(nums) - 1
        _sum = 0
        diff = float('inf')
        w.... left < right:
            _sum = nums[left] + nums[right]
            __ _sum < target:
                diff = m..(diff, target - _sum)
                left += 1
            ____:
                diff = m..(diff, _sum - target)
                right -= 1

        r.. diff
