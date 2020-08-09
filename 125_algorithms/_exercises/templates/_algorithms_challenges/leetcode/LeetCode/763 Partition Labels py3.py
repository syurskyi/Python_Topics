#!/usr/bin/python3
"""
A string S of lowercase letters is given. We want to partition this string into
as many parts as possible so that each letter appears in at most one part, and
return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits
S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""
from typing ______ List


class Solution:
    ___ partitionLabels(self, S: str) -> List[int]:
        lasts = {}
        n = le.(S)
        ___ i in range(n-1, -1, -1
            __ S[i] not in lasts:
                lasts[S[i]] = i

        indexes = [-1]  # last partition ending index
        cur_last = 0
        ___ i in range(n
            cur_last = max(cur_last, lasts[S[i]])
            __ cur_last __ i:
                indexes.append(cur_last)

        ret = []
        ___ i in range(le.(indexes) - 1
            ret.append(indexes[i+1] - indexes[i])
        r_ ret


__ __name__ __ "__main__":
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") __ [9, 7, 8]
