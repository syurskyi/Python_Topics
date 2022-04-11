c_ Solution:
    ___ nextPermutation  nums
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        __ n.. nums o. l..(nums) < 2:
            r.. nums

        n l..(nums)
        i n - 2
        w.... i >_ 0 a.. nums[i] >_ nums[i + 1]:
            i -_ 1

        __ i >_ 0:
            j n - 1
            w.... i < j a.. nums[i] >_ nums[j]:
                j -_ 1
            nums[i], nums[j] nums[j], nums[i]

        i i + 1
        j n - 1
        w.... i < j:
            nums[i], nums[j] nums[j], nums[i]
            i += 1
            j -_ 1
