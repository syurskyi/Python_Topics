#!/usr/bin/python3
"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""
____ c.. _______ Counter


c_ Solution:
    ___ findAnagrams(self, s, target):
        """
        Brute force: O(|target|) * O(cmp) * O(|s|)
        Counter: O(cmp) * O(|s|)
        where O(cmp) = 26, the length of alphabeta
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret    # list
        counter_target = Counter(target)
        counter_cur = Counter(s[:l..(target)])
        __ counter_cur __ counter_target:
            ret.a..(0)

        ___ idx __ r..(l..(target), l..(s)):
            head = s[idx - l..(target)]
            tail = s[idx]
            counter_cur[tail] += 1
            counter_cur[head] -= 1
            __ counter_cur[head] __ 0:
                del counter_cur[head]  # requried for comparison
            __ counter_cur __ counter_target:
                # idx is the ending index, find the starting
                ret.a..(idx - l..(target) + 1)

        r.. ret


__ _______ __ _______
    ... Solution().findAnagrams("cbaebabacd", "abc") __ [0, 6]
