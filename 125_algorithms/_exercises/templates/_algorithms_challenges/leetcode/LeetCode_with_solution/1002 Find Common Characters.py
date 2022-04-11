#!/usr/bin/python3
"""
Given an array A of strings made only from lowercase letters, return a list of
all characters that show up in all strings within the list (including
duplicates).  For example, if a character occurs 3 times in all strings but not
4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""
_______ s__

____ t___ _______ L..
____ c.. _______ C..


c_ Solution:
    ___ commonChars  A: L..[s..]) __ L..[s..]:
        """
        running counter
        """
        ret    # list
        __ n.. A:
            r.. ret
            
        counter C..(A[0])
        ___ a __ A[1:]:
            cur C..(a)
            ___ c __ s__.a..:
                counter[c] m..(counter[c], cur[c])

        ___ c __ s__.a..:
            __ counter[c] > 0:
                ret.e.. [c] * counter[c])

        r.. ret
