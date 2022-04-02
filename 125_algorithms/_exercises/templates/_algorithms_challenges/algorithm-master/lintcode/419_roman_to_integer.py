c_ Solution:
    ___ romanToInt  s
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        __ n.. s:
            r.. ans

        symbs = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        ans += symbs[s[-1]]

        ___ i __ r..(l..(s) - 2, -1, -1
            __ symbs[s[i]] >= symbs[s[i + 1]]:
                ans += symbs[s[i]]
            ____:
                ans -= symbs[s[i]]

        r.. ans
