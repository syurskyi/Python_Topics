class Solution:
    ___ minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        __ n.. s o. n.. t:
            r.. ''

        F = {}
        ___ c __ t:
            F[c] = F.get(c, 0) + 1

        n, cnt = l..(s), l..(F)
        start = size = INFINITY = float('inf')
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

                __ right - left < size:
                    size = right - left
                    start = left

                left += 1

        r.. s[start:start + size] __ size < INFINITY ____ ''
