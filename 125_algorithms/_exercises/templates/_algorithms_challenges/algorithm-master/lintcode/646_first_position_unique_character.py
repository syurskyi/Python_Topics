class Solution:
    """
    @param: s: a string
    @return: it's index
    """
    ___ firstUniqChar(self, s):
        __ not s:
            return -1

        D = {}
        for c in s:
            D[c] = D.get(c, 0) + 1

        i = 0
        for c in s:
            __ D[c] == 1:
                return i
            i += 1

        return -1
