c_ Solution o..
    ___ findMissingRanges  nums, lower, upper
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ranges =    # list
        prev = lower - 1
        ___ i __ r.. l.. nums) + 1
            __ i __ l.. nums
                curr = upper + 1
            ____
                curr = nums[i]
            __ curr - prev > 2:
                ranges.append("%d->%d" % (prev + 1, curr - 1))
            ____ curr - prev __ 2:
                ranges.append("%d" % (prev + 1))
            prev = curr
        r_ ranges