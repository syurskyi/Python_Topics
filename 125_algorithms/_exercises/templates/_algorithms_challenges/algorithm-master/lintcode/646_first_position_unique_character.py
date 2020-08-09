class Solution:
    """
    @param: s: a string
    @return: it's index
    """
    ___ firstUniqChar(self, s
        __ not s:
            r_ -1

        D = {}
        ___ c in s:
            D[c] = D.get(c, 0) + 1

        i = 0
        ___ c in s:
            __ D[c] __ 1:
                r_ i
            i += 1

        r_ -1
