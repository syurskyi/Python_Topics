______ collections


class Solution:
    ___ lengthOfLongestSubstring(self, s
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        __ not s:
            r_ ans

        freqs = collections.defaultdict(int)
        i = rep = 0

        for j in range(le.(s)):
            __ freqs[s[j]] __ 1:
                rep += 1
            freqs[s[j]] += 1

            w___ rep > 0:
                freqs[s[i]] -= 1
                __ freqs[s[i]] __ 1:
                    rep -= 1

                i += 1

            ans = max(ans, j - i + 1)

        r_ ans
