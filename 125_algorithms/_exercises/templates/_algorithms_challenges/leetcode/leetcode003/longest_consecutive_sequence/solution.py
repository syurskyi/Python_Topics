class Solution:
    # @param num, a list of integer
    # @return an integer
    ___ longestConsecutive(self, num
        __ not num:
            r_ 0
        d = {}
        ___ e in num:
            __ e not in d:
                d[e] = 1
        res = 1
        ___ c in num:
            current = 1
            __ c not in d:
                continue
            w___ c - 1 in d:
                c -= 1
            del d[c]
            w___ c + 1 in d:
                c += 1
                current += 1
                del d[c]
            res = max(res, current)
        r_ res
