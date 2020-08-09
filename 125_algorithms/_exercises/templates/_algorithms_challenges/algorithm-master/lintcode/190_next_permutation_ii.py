class Solution:
    ___ nextPermutation(self, nums
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        __ not nums or le.(nums) < 2:
            r_ nums

        n = le.(nums)
        i = n - 2
        w___ i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        __ i >= 0:
            j = n - 1
            w___ i < j and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        i = i + 1
        j = n - 1
        w___ i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
