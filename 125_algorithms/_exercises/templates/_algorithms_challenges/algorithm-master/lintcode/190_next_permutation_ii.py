c_ Solution:
    ___ nextPermutation(self, nums):
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        __ n.. nums o. l..(nums) < 2:
            r.. nums

        n = l..(nums)
        i = n - 2
        w.... i >= 0 a.. nums[i] >= nums[i + 1]:
            i -= 1

        __ i >= 0:
            j = n - 1
            w.... i < j a.. nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        i = i + 1
        j = n - 1
        w.... i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
