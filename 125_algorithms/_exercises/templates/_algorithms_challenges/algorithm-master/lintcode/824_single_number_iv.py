c_ Solution:
    ___ getSingleNumber  nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        __ n.. nums:
            r.. -1

        __ l..(nums) __ 1:
            r.. nums[0]

        n = l..(nums)
        left, right = 0, n - 1

        w.... left + 1 < right:
            mid = (left + right) // 2
            __ mid > 0 a.. nums[mid] __ nums[mid - 1]:
                __ mid & 1 __ 1:
                    left = mid
                ____:
                    right = mid
            ____:
                __ mid & 1 __ 1:
                    right = mid
                ____:
                    left = mid

        ___ mid __ (left, right):
            __ mid > 0 a.. nums[mid] __ nums[mid - 1]:
                _____
            __ mid + 1 < n a.. nums[mid] __ nums[mid + 1]:
                _____
            r.. nums[mid]

        r.. -1
