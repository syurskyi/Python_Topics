class Solution:
    # @return an integer
    ___ lengthOfLongestSubstring(self, s
        res = 0
        cur = 0
        d = {}
        ___ i, c __ enumerate(s
            __ c not __ d:
                cur += 1
            ____
                cur = min(i - d[c], cur + 1)
            d[c] = i
            res = ma.(res, cur)
        r_ res
