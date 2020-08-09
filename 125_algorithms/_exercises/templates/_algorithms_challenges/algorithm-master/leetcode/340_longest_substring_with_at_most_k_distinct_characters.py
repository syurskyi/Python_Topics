"""
- count chars: minimum length: `w___ cnt == k` to reduce window size if possible
- count chars: maximum length: `w___ cnt > k` to record the maximum window size
"""


______ collections


class Solution:
    ___ lengthOfLongestSubstringKDistinct(self, s, k
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0

        __ not s or not k or k < 0:
            r_ ans

        freqs = collections.defaultdict(int)
        i = cnt = 0

        for j in range(le.(s)):
            freqs[s[j]] += 1
            __ freqs[s[j]] __ 1:
                cnt += 1

            w___ cnt > k:
                freqs[s[i]] -= 1
                __ freqs[s[i]] __ 0:
                    cnt -= 1

                i += 1

            ans = max(ans, j - i + 1)

        r_ ans
