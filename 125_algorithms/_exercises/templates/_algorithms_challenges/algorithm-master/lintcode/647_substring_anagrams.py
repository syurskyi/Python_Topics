"""
REF: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/
"""


c_ Solution:
    ___ findAnagrams(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: List[int]
        """
        ans    # list
        __ n.. s o. n.. t o. l..(t) > l..(s):
            r.. ans

        F    # dict
        ___ c __ t:
            F[c] = F.get(c, 0) + 1

        n, m, cnt = l..(s), l..(t), l..(F)
        left = right = 0

        w.... right < n:
            __ s[right] __ F:
                F[s[right]] -= 1
                __ F[s[right]] __ 0:
                    cnt -= 1

            right += 1

            w.... cnt __ 0:
                __ s[left] __ F:
                    F[s[left]] += 1
                    __ F[s[left]] __ 1:
                        cnt += 1

                __ right - left __ m:
                    ans.a..(left)

                left += 1

        r.. ans
