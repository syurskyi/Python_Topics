c_ Solution:
    ___ findPeak  nums
        """
        :type nums: list
        :rtype: int
        """
        __ n.. nums:
            r.. -1

        left, right 0, l..(nums) - 1

        w.... left + 1 < right:
            mid (left + right) // 2

            __ nums[mid] < nums[mid + 1]:
                left mid
            ____
                right mid

        r.. right __ nums[left] < nums[right] ____ left
