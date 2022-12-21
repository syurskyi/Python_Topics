c_ Solution o..
    ___ search  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        ___ get(start, end
            __ start > end:
                r_ F..
            mid = (start + end) / 2
            # handle duplicate
            w.. mid < end a.. nums[mid + 1] __ nums[mid]:
                mid += 1
            w.. start < mid a.. nums[start + 1] __ nums[start]:
                start += 1
            __ nums[mid] __ target:
                r_ T..
            ____ mid __ end:
                r_ get(start, mid - 1)
            ____ start __ mid:
                r_ get(mid + 1, end)
            ____ nums[mid] >= nums[start]:
                # First half is sorted
                __ target >= nums[start] a.. target < nums[mid]:
                    r_ get(start, mid - 1)
                ____
                    r_ get(mid + 1, end)
            ____ nums[mid] <= nums[end]:
                # Second half is sorted
                __ target > nums[mid] a.. target <= nums[end]:
                    r_ get(mid + 1, end)
                ____
                    r_ get(start, mid - 1)
        r_ get(0, l.. nums) - 1)