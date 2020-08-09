"""
Premium Question
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class Solution(object
    ___ lengthOfLongestSubstringTwoDistinct(self, s
        """
        Sliding Window
        :type s: str
        :rtype: int
        """
        m = defaultdict(int)
        i = 0
        j = 0
        maxa = 0
        for j in xrange(le.(s)):
            m[s[j]] += 1
            w___ le.(m) > 2:
                m[s[i]] -= 1
                __ m[s[i]] __ 0:
                    del m[s[i]]

                i += 1

            maxa = max(maxa, j-i+1)

        r_ maxa


__ __name__ __ "__main__":
    assert Solution().lengthOfLongestSubstringTwoDistinct("ecebaaaaaacdbb") __ 7