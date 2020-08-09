class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    ___ lastPosition(self, nums, target
        __ not nums or not target:
            r_ -1

        l, m, r = 0, 0, le.(nums) - 1
        w___ l + 1 < r:
            m = l + (r - l) // 2
            __ nums[m] > target:
                r = m
            ____
                l = m

        """
        considering the edge case: [1, 1, 1, 1]
        we've compared all child above but the both ends
        so we should check the both ends
        """
        __ nums[r] __ target:
            r_ r
        ____ nums[l] __ target:
            r_ l
        ____
            r_ -1
