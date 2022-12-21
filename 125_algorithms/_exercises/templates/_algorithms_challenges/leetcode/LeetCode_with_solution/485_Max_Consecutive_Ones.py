c_ Solution o..
    ___ findMaxConsecutiveOnes  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        curr = 0
        ___ n __ nums:
            __ n __ 1:
                # Add 1 to curr when encounter 1
                curr += 1
                __ curr > ans:
                    ans = curr
            ____
                # Add 1 to curr when encounter 1
                curr = 0
        r_ ans
