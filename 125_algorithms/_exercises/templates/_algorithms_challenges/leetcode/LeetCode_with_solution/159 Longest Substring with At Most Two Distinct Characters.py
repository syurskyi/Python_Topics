"""
Premium Question
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


c_ Solution(object):
    ___ lengthOfLongestSubstringTwoDistinct(self, s):
        """
        Sliding Window
        :type s: str
        :rtype: int
        """
        m = defaultdict(int)
        i = 0
        j = 0
        maxa = 0
        ___ j __ xrange(l..(s)):
            m[s[j]] += 1
            w.... l..(m) > 2:
                m[s[i]] -= 1
                __ m[s[i]] __ 0:
                    del m[s[i]]

                i += 1

            maxa = max(maxa, j-i+1)

        r.. maxa


__ __name__ __ "__main__":
    ... Solution().lengthOfLongestSubstringTwoDistinct("ecebaaaaaacdbb") __ 7