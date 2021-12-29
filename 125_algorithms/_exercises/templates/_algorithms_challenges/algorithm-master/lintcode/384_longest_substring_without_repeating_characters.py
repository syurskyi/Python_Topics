import collections


class Solution:
    ___ lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        __ not s:
            return ans

        freqs = collections.defaultdict(int)
        i = rep = 0

        for j in range(len(s)):
            __ freqs[s[j]] == 1:
                rep += 1
            freqs[s[j]] += 1

            while rep > 0:
                freqs[s[i]] -= 1
                __ freqs[s[i]] == 1:
                    rep -= 1

                i += 1

            ans = max(ans, j - i + 1)

        return ans
