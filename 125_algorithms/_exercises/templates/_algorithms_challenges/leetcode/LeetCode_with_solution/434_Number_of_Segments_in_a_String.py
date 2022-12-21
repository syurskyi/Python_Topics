c_ Solution o..
    # https://leetcode.com/problems/number-of-segments-in-a-string/solution/
    # def countSegments(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     return len(s.split())

    ___ countSegments  s
         segment_count = 0
        ___ i __ r.. l.. s)):
            __ (i __ 0 or s[i-1] __ ' ') a.. s[i] != ' ':
                segment_count += 1

        r_ segment_count