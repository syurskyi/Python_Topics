"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = "eceba" and k = 2,

T is "ece" which its length is 3.

Show Company Tags
Show Tags
Show Similar Problems
"""
____ c.. _______ d..

__author__ = 'Daniel'


c_ Solution(o..
    ___ lengthOfLongestSubstringKDistinct  s, k
        """
        Brute force: O(n^2 * n)

        Sliding window O(n)
        :type s: str
        :type k: int
        :rtype: int
        """
        st = 0  # start
        counter = d..(i..)
        maxa = 0
        ___ idx, val __ e..(s
            __ counter[val] __ 0:
                k -_ 1

            counter[val] += 1
            w.... k < 0:
                counter[s[st]] -_ 1
                __ counter[s[st]] __ 0:
                    k += 1
                st += 1

            maxa = m..(maxa, idx - st + 1)

        r.. maxa


__ _______ __ _______
    ... Solution().lengthOfLongestSubstringKDistinct("eceba", 2) __ 3
