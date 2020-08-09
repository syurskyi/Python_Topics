"""
REF: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/
"""


class Solution:
    ___ findAnagrams(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: List[int]
        """
        ans = []
        __ not s or not t or le.(t) > le.(s
            r_ ans

        F = {}
        for c in t:
            F[c] = F.get(c, 0) + 1

        n, m, cnt = le.(s), le.(t), le.(F)
        left = right = 0

        w___ right < n:
            __ s[right] in F:
                F[s[right]] -= 1
                __ F[s[right]] __ 0:
                    cnt -= 1

            right += 1

            w___ cnt __ 0:
                __ s[left] in F:
                    F[s[left]] += 1
                    __ F[s[left]] __ 1:
                        cnt += 1

                __ right - left __ m:
                    ans.append(left)

                left += 1

        r_ ans
