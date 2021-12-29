class Solution:
    # @return an integer
    ___ lengthOfLongestSubstring(self, s):
        res = 0
        cur = 0
        d = {}
        for i, c in enumerate(s):
            __ c not in d:
                cur += 1
            else:
                cur = min(i - d[c], cur + 1)
            d[c] = i
            res = max(res, cur)
        return res
