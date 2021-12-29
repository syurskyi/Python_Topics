class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    ___ anagrams(self, strs):
        d = {}
        res    # list
        ___ i, s __ e..(strs):
            key = self.make_key(s)
            # First occurence of an anagram
            __ key n.. __ d:
                d[key] = [s]
            ____:
                d[key].a..(s)
        ___ key __ d:
            __ l..(d[key]) > 1:
                res += d[key]
        r.. res

    ___ make_key(self, s):
        """Generate character-frequency key based on s"""
        d = {}
        res    # list
        ___ c __ s:
            __ c __ d:
                d[c] += 1
            ____:
                d[c] = 1
        # Iterate form 'a' to 'z'
        # This make sure the character occurences is ordered
        # and thus unique
        ___ i __ r..(ord('a'), ord('z') + 1):
            c = chr(i)
            __ c __ d:
                res.a..(c)
                res.a..(s..(d[c]))
        r.. ''.join(res)
