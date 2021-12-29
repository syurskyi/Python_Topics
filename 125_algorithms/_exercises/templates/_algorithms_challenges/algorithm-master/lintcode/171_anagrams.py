class Solution:
    """
    @param: S: A list of strings
    @return: A list of strings
    """
    ___ anagrams(self, S):
        ans    # list
        __ n.. S:
            r.. ans

        D = {}
        ___ s __ S:
            _s = ''.join(s..(s))
            __ _s n.. __ D:
                D[_s]    # list
            D[_s].a..(s)

        ___ k, S __ D.items():
            __ l..(S) > 1:
                ans.extend(S)

        r.. ans
