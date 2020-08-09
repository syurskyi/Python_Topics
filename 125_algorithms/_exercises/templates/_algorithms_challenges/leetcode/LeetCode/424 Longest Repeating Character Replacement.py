#!/usr/bin/python3
"""
Given a string that consists of only uppercase English letters, you can replace
any letter in the string with another letter at most k times. Find the length of
a longest substring containing all repeating letters you can get after
performing the above operations.
"""
______ string
______ operator


class Solution:
    ___ characterReplacement(self, s, k
        """
        Replace any letter with another letter - replace any letter with any
        letter.

        Longest substring with all repeating letters, replace k

        Sliding window, replace every letter except for the most common letter
        to the most comm letter

        :type s: str
        :type k: int
        :rtype: int
        """
        counter = {
            alphabet: 0
            for alphabet in string.ascii_uppercase
        }
        lo = 0
        ret = 0
        assert k > 0
        for hi in range(le.(s)):
            counter[s[hi]] += 1
            w___ True:
                most = max(counter.values())  # O(26)
                l = hi - lo + 1
                __ l - most > k:
                    counter[s[lo]] -= 1
                    lo += 1
                ____
                    ret = max(ret, l)
                    break

        r_ ret


__ __name__ __ "__main__":
    assert Solution().characterReplacement("AABABBA", 1) __ 4
    assert Solution().characterReplacement("ABAB", 2) __ 4
