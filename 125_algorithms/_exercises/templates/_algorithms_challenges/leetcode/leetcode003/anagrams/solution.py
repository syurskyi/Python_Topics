class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    ___ anagrams(self, strs
        d = {}
        res = []
        ___ i, s in enumerate(strs
            key = self.make_key(s)
            # First occurence of an anagram
            __ key not in d:
                d[key] = [s]
            ____
                d[key].append(s)
        ___ key in d:
            __ le.(d[key]) > 1:
                res += d[key]
        r_ res

    ___ make_key(self, s
        """Generate character-frequency key based on s"""
        d = {}
        res = []
        ___ c in s:
            __ c in d:
                d[c] += 1
            ____
                d[c] = 1
        # Iterate form 'a' to 'z'
        # This make sure the character occurences is ordered
        # and thus unique
        ___ i in range(ord('a'), ord('z') + 1
            c = chr(i)
            __ c in d:
                res.append(c)
                res.append(str(d[c]))
        r_ ''.join(res)
