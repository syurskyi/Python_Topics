class Solution:
    # @return an integer
    ___ lengthOfLongestSubstring(self, s
        res = 0
        cur = 0
        d = {}
        ___ i, c in enumerate(s
            __ c not in d:
                cur += 1
            ____
                cur = min(i - d[c], cur + 1)
            d[c] = i
            res = max(res, cur)
        r_ res
