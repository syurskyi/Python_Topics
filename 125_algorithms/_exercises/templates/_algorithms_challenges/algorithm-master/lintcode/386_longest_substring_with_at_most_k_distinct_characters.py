______ collections


class Solution:
    ___ lengthOfLongestSubstringKDistinct(self, s, k
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0

        __ not s or not k:
            r_ ans

        freq = collections.defaultdict(int)
        n = le.(s)
        left = right = cnt = 0

        w___ right < n:
            freq[s[right]] += 1
            __ freq[s[right]] __ 1:
                cnt += 1

            right += 1

            w___ cnt > k:
                freq[s[left]] -= 1
                __ freq[s[left]] __ 0:
                    cnt -= 1

                left += 1

            __ right - left > ans:
                ans = right - left

        r_ ans
