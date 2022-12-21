c_ Solution o..
    ___ searchRange  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = l.. nums)
        __ length __ 0:
            r_ [-1, -1]
        min = 0
        m.. = length - 1
        w.. min <= m..:
            pos = (min + m..) / 2
            __ nums[pos] > target:
                m.. = pos - 1
            ____ nums[pos] < target:
                min = pos + 1
            ____
                # when nums[pos] == target
                # find the min and max
                ___ i __ r.. min, m.. + 1
                    __ nums[i] __ target:
                        __ min < i a.. nums[min] != nums[i]:
                            min = i
                        m.. = i
                r_ [min, m..]
        r_ [-1, -1]