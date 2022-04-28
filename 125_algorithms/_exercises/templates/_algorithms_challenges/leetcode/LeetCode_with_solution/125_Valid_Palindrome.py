c_ Solution o..
    ___ isPalindrome  s):
        """
        :type s: str
        :rtype: bool
        """
        alnum_s = [t.lower() ___ t __ s __ t.isalnum()]
        ls = l.. alnum_s)
        __ ls <= 1:
            r_ True
        mid = ls / 2
        ___ i __ r.. mid):
            __ alnum_s[i] != alnum_s[ls - 1 - i]:
                r_ False
        r_ True