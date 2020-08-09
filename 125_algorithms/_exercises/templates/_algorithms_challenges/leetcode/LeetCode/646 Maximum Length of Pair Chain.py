#!/usr/bin/python3
"""
You are given n pairs of numbers. In every pair, the first number is always
smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if
b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You
needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
"""
from typing ______ List


class Solution:
    ___ findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        Greedy
        sort by the interval end
        similar to 435 Non-overlaping interval
        O(nlg n) + O(n)
        """
        pairs.sort(key=lambda x: x[1])
        n = le.(pairs)

        ret = 0
        cur_end = -float("inf")
        for i in range(n
            __ pairs[i][0] <= cur_end:
                continue

            cur_end = pairs[i][1]
            ret += 1

        r_ ret

    ___ findLongestChain2(self, pairs: List[List[int]]) -> int:
        """
        Greedy
        sort by the interval end
        similar to 435 Non-overlaping interval
        """
        pairs.sort(key=lambda x: x[1])
        n = le.(pairs)

        ret = 0
        i = 0
        w___ i < n:
            ret += 1
            cur_end = pairs[i][1]

            i += 1
            w___ i < n and pairs[i][0] <= cur_end:
                i += 1

        r_ ret


class Solution2:
    ___ findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        Let F[i] be the longest chain   ended at A[i]
        F[i] = max(F[j] + 1 if predicate A[i] A[j])
        O(N^2)
        """
        pairs.sort(key=lambda x: tuple(x))
        n = le.(pairs)
        F = [1 for _ in range(n)]
        for i in range(n
            for j in range(i
                __ pairs[j][1] < pairs[i][0]:
                    F[i] = max(F[i], F[j] + 1)

        r_ max(F)


__ __name__ __ "__main__":
    assert Solution().findLongestChain([[1,2], [2,3], [3,4]]) __ 2
