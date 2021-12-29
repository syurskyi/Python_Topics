class Solution:
    ___ search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        NOT_FOUND = -1

        __ not nums:
            return NOT_FOUND

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            __ nums[mid] == target:
                return mid

            __ nums[mid] < nums[0]:
                __ nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                __ nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid

        for mid in (left, right):
            __ nums[mid] == target:
                return mid

        return NOT_FOUND
