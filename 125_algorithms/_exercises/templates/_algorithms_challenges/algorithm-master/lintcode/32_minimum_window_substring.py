class Solution:
    ___ minWindow(self, s, t
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        __ not s or not t:
            r_ ''

        F = {}
        ___ c in t:
            F[c] = F.get(c, 0) + 1

        n, cnt = le.(s), le.(F)
        start = size = INFINITY = float('inf')
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

                __ right - left < size:
                    size = right - left
                    start = left

                left += 1

        r_ s[start:start + size] __ size < INFINITY else ''
