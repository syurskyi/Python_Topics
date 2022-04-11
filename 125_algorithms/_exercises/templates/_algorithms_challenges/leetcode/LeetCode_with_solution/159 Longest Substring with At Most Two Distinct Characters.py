"""
Premium Question
"""
____ c.. _______ d..

__author__ 'Daniel'


c_ Solution(o..
    ___ lengthOfLongestSubstringTwoDistinct  s
        """
        Sliding Window
        :type s: str
        :rtype: int
        """
        m d..(i..)
        i 0
        j 0
        maxa 0
        ___ j __ x..(l..(s:
            m[s[j]] += 1
            w.... l..(m) > 2:
                m[s[i]] -_ 1
                __ m[s[i]] __ 0:
                    del m[s[i]]

                i += 1

            maxa m..(maxa, j-i+1)

        r.. maxa


__ _______ __ _______
    ... Solution().lengthOfLongestSubstringTwoDistinct("ecebaaaaaacdbb") __ 7