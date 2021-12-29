class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    ___ lastPosition(self, nums, target):
        __ n.. nums o. n.. target:
            r.. -1

        l, m, r = 0, 0, l..(nums) - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            __ nums[m] > target:
                r = m
            ____:
                l = m

        """
        considering the edge case: [1, 1, 1, 1]
        we've compared all child above but the both ends
        so we should check the both ends
        """
        __ nums[r] __ target:
            r.. r
        ____ nums[l] __ target:
            r.. l
        ____:
            r.. -1
