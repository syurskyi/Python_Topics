c_ Solution:
    # @return an integer
    ___ lengthOfLongestSubstring  s
        res = 0
        cur = 0
        d    # dict
        ___ i, c __ e..(s
            __ c n.. __ d:
                cur += 1
            ____
                cur = m..(i - d[c], cur + 1)
            d[c] = i
            res = m..(res, cur)
        r.. res
