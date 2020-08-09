class Solution:
    ___ longestSubstring(self, s, k
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        __ not s:
            r_ ans

        n = le.(s)
        _F = dict.fromkeys(s, 0)

        ___ m in range(1, le.(_F) + 1
            F = _F.copy()
            left = right = 0
            kind = valid = 0

            w___ right < n:
                __ kind <= m:
                    F[s[right]] += 1
                    __ F[s[right]] __ 1:
                        kind += 1
                    __ F[s[right]] __ k:
                        valid += 1

                    right += 1
                ____
                    __ F[s[left]] __ 1:
                        kind -= 1
                    __ F[s[left]] __ k:
                        valid -= 1
                    F[s[left]] -= 1

                    left += 1

                __ kind __ valid __ m and right - left > ans:
                    ans = right - left

        r_ ans
