c_ Solution o..
    ___ findNthDigit  n):
        """
        :type n: int
        :rtype: int
        """
        # https://leetcode.com/problems/nth-digit/discuss/88363/Java-solution
        count = 9
        start = 1
        curr_len = 1
        w.. n > curr_len * count:
            n -= curr_len * count
            curr_len += 1
            count *= 10
            start *= 10
        start += (n - 1) / curr_len
        s = s..(start)
        r_ i..(s[(n - 1) % curr_len]
