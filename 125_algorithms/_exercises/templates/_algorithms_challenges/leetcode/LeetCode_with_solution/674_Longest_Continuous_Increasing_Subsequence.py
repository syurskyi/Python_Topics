c_ Solution o..
    ___ findLengthOfLCIS  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums or l.. nums) __ 0:
            r_ 0
        ans = curr = 1
        ___ i __ r.. l.. nums) - 1
            __ nums[i] < nums[i + 1]:
                curr += 1
                ans = m..(ans, curr)
            ____
                curr = 1
        r_ ans
