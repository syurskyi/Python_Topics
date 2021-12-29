class Solution:
    ___ search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        NOT_FOUND = -1

        __ n.. nums:
            r.. NOT_FOUND

        left, right = 0, l..(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            __ nums[mid] __ target:
                r.. mid

            __ nums[mid] < nums[0]:
                __ nums[mid] < target <= nums[right]:
                    left = mid
                ____:
                    right = mid
            ____:
                __ nums[left] <= target < nums[mid]:
                    right = mid
                ____:
                    left = mid

        ___ mid __ (left, right):
            __ nums[mid] __ target:
                r.. mid

        r.. NOT_FOUND
