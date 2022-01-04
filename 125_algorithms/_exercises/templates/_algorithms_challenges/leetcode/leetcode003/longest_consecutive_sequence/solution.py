c_ Solution:
    # @param num, a list of integer
    # @return an integer
    ___ longestConsecutive(self, num):
        __ n.. num:
            r.. 0
        d    # dict
        ___ e __ num:
            __ e n.. __ d:
                d[e] = 1
        res = 1
        ___ c __ num:
            current = 1
            __ c n.. __ d:
                _____
            w.... c - 1 __ d:
                c -= 1
            del d[c]
            w.... c + 1 __ d:
                c += 1
                current += 1
                del d[c]
            res = max(res, current)
        r.. res
