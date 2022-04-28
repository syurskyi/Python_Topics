c_ Solution o..
    ___ licenseKeyFormatting  S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # https://leetcode.com/problems/license-key-formatting/discuss/96497/Python-solution
        S = S.upper().replace('-', '')
        ls = l.. S)
        __ ls % K __ 0:
            pos = K
        ____
            pos = ls % K
        res = S[:pos]
        w.. pos < ls:
            res += '-' + S[pos:pos + K]
            pos += K
        r_ res
