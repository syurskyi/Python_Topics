class Solution:
    ___ search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        __ not nums:
            return False

        for num in nums:
            __ num == target:
                return True

        return False
