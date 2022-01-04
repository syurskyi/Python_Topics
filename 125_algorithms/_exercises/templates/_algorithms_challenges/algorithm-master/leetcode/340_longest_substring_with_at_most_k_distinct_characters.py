"""
- count chars: minimum length: `while cnt == k` to reduce window size if possible
- count chars: maximum length: `while cnt > k` to record the maximum window size
"""


_______ collections


c_ Solution:
    ___ lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0

        __ n.. s o. n.. k o. k < 0:
            r.. ans

        freqs = collections.defaultdict(i..)
        i = cnt = 0

        ___ j __ r..(l..(s)):
            freqs[s[j]] += 1
            __ freqs[s[j]] __ 1:
                cnt += 1

            w.... cnt > k:
                freqs[s[i]] -= 1
                __ freqs[s[i]] __ 0:
                    cnt -= 1

                i += 1

            ans = max(ans, j - i + 1)

        r.. ans
