_______ c..


c_ Solution:
    ___ lengthOfLongestSubstringKDistinct  s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0

        __ n.. s o. n.. k:
            r.. ans

        freq = c...defaultdict(i..)
        n = l..(s)
        left = right = cnt = 0

        w.... right < n:
            freq[s[right]] += 1
            __ freq[s[right]] __ 1:
                cnt += 1

            right += 1

            w.... cnt > k:
                freq[s[left]] -= 1
                __ freq[s[left]] __ 0:
                    cnt -= 1

                left += 1

            __ right - left > ans:
                ans = right - left

        r.. ans
