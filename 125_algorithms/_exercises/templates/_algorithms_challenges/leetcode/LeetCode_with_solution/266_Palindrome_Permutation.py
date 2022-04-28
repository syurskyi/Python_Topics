c_ Solution o..
    ___ canPermutePalindrome  s):
        """
        :type s: str
        :rtype: bool
        """
        dic  # dict
        ___ c __ s:
            dic[c] = dic.get(c, 0) + 1
        odd, even = 0, 0
        ___ c __ dic:
            __ dic[c] % 2 __ 0:
                even += 1
            ____
                odd += 1
        __ odd <= 1:
            r_ True
        r_ False
