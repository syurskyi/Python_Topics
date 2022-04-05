_______ c..


c_ Solution:
    ___ lengthOfLongestSubstring  s
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        __ n.. s:
            r.. ans

        freqs = c...d..(i..)
        i = rep = 0

        ___ j __ r..(l..(s:
            __ freqs[s[j]] __ 1:
                rep += 1
            freqs[s[j]] += 1

            w.... rep > 0:
                freqs[s[i]] -_ 1
                __ freqs[s[i]] __ 1:
                    rep -_ 1

                i += 1

            ans = m..(ans, j - i + 1)

        r.. ans
