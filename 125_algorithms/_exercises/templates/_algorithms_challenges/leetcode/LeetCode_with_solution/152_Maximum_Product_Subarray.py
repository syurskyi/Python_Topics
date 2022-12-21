c_ Solution o..
    ___ maxProduct  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ nums is N.. or l.. nums) __ 0:
            r_ 0
        max_here = min_here = max_so_far = nums[0]
        ___ i __ r.. 1, l.. nums)):
            mx, mn = max_here, min_here
            max_here = m..(m..(mx * nums[i], nums[i]), mn * nums[i])
            min_here = min(min(mx * nums[i], nums[i]), mn * nums[i])
            max_so_far = m..(max_here, max_so_far)
        r_ max_so_far