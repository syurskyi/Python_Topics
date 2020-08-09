"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = "eceba" and k = 2,

T is "ece" which its length is 3.

Show Company Tags
Show Tags
Show Similar Problems
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class Solution(object
    ___ lengthOfLongestSubstringKDistinct(self, s, k
        """
        Brute force: O(n^2 * n)

        Sliding window O(n)
        :type s: str
        :type k: int
        :rtype: int
        """
        st = 0  # start
        counter = defaultdict(int)
        maxa = 0
        ___ idx, val in enumerate(s
            __ counter[val] __ 0:
                k -= 1

            counter[val] += 1
            w___ k < 0:
                counter[s[st]] -= 1
                __ counter[s[st]] __ 0:
                    k += 1
                st += 1

            maxa = max(maxa, idx - st + 1)

        r_ maxa


__ __name__ __ "__main__":
    assert Solution().lengthOfLongestSubstringKDistinct("eceba", 2) __ 3
