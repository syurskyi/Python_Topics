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
import string

from typing import List
from collections import Counter


class Solution:
    ___ commonChars(self, A: List[str]) -> List[str]:
        """
        running counter
        """
        ret = []
        __ not A:
            return ret
            
        counter = Counter(A[0])
        for a in A[1:]:
            cur = Counter(a)
            for c in string.ascii_lowercase:
                counter[c] = min(counter[c], cur[c])

        for c in string.ascii_lowercase:
            __ counter[c] > 0:
                ret.extend([c] * counter[c])

        return ret
