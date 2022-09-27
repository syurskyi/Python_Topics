c_ Solution o..
    # def isAnagram(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     # sort
    #     return sorted(s) == sorted(t)

    ___ isAnagram  s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # hash
        # https://leetcode.com/articles/valid-anagram/
        __ l.. s) != l.. t):
            r_ F..
        counter = [0] * 26
        ___ i __ r.. l.. s)):
            counter[o.. s[i]) - o.. 'a')] += 1
            counter[o.. t[i]) - o.. 'a')] -= 1
        ___ num __ counter:
            __ num != 0:
                r_ F..
        r_ T..