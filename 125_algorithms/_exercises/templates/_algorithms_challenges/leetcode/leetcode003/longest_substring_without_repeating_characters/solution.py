class Solution:
    # @return an integer
    ___ lengthOfLongestSubstring(self, s):
        res = 0
        cur = 0
        d = {}
        ___ i, c __ enumerate(s):
            __ c n.. __ d:
                cur += 1
            ____:
                cur = m..(i - d[c], cur + 1)
            d[c] = i
            res = max(res, cur)
        r.. res
