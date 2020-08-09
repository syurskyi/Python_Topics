#!/usr/bin/python3
"""
Return all non-negative integers of length N such that the absolute difference
between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the
number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:

1 <= N <= 9
0 <= K <= 9
"""
from typing ______ List


class Solution:
    ___ __init__(self
        self.cache = {}

    ___ numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        """
        dfs + memoization
        """
        ret = []
        ___ i in range(1, 10
            ret.extend(self.dfs(i, N, K))

        __ N __ 1:
            ret.append([0])  # special case

        r_ list(
            map(lambda x: int("".join(map(str, x))), ret)
        )

    ___ dfs(self, start: int, N: int, K: int) -> List[List[int]]:
        __ (start, N, K) not in self.cache:
            ret = []
            __ N __ 1:
                ret = [[start]]
            ____ N > 1:
                __ start + K <= 9:
                    ___ e in self.dfs(start + K, N - 1, K
                        ret.append([start] + e)
                __ start - K >= 0 and K != 0:  # special case
                    ___ e in self.dfs(start - K, N - 1, K
                        ret.append([start] + e)

            self.cache[start, N, K] = ret

        r_ self.cache[start, N, K]


__ __name__ __ "__main__":
    Solution().numsSameConsecDiff(3, 7) __ [181,292,707,818,929]
