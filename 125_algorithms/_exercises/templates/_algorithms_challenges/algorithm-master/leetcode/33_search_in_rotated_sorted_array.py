c_ Solution:
    ___ s..  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N.. -1

        __ n.. nums:
            r.. N..

        left, right 0, l..(nums) - 1

        w.... left + 1 < right:
            mid (left + right) // 2

            __ nums[mid] __ target:
                r.. mid

            __ nums[mid] < nums[0]:
                __ nums[mid] < target <_ nums[right]:
                    left mid
                ____
                    right mid
            ____
                __ nums[left] <_ target < nums[mid]:
                    right mid
                ____
                    left mid

        ___ mid __ (left, right
            __ nums[mid] __ target:
                r.. mid

        r.. N..
