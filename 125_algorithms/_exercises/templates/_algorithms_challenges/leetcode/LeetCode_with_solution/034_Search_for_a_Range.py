c_ Solution o..
    ___ searchRange  nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = l.. nums)
        __ length __ 0:
            r_ [-1, -1]
        min = 0
        max = length - 1
        w.. min <= max:
            pos = (min + max) / 2
            __ nums[pos] > target:
                max = pos - 1
            ____ nums[pos] < target:
                min = pos + 1
            ____
                # when nums[pos] == target
                # find the min and max
                ___ i __ r.. min, max + 1):
                    __ nums[i] __ target:
                        __ min < i and nums[min] != nums[i]:
                            min = i
                        max = i
                r_ [min, max]
        r_ [-1, -1]