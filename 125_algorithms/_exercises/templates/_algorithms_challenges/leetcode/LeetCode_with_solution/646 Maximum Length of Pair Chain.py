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
____ typing _______ List


c_ Solution:
    ___ findLongestChain(self, pairs: List[List[i..]]) __ i..:
        """
        Greedy
        sort by the interval end
        similar to 435 Non-overlaping interval
        O(nlg n) + O(n)
        """
        pairs.s..(key=l.... x: x[1])
        n = l..(pairs)

        ret = 0
        cur_end = -float("inf")
        ___ i __ r..(n):
            __ pairs[i][0] <= cur_end:
                _____

            cur_end = pairs[i][1]
            ret += 1

        r.. ret

    ___ findLongestChain2(self, pairs: List[List[i..]]) __ i..:
        """
        Greedy
        sort by the interval end
        similar to 435 Non-overlaping interval
        """
        pairs.s..(key=l.... x: x[1])
        n = l..(pairs)

        ret = 0
        i = 0
        w.... i < n:
            ret += 1
            cur_end = pairs[i][1]

            i += 1
            w.... i < n a.. pairs[i][0] <= cur_end:
                i += 1

        r.. ret


c_ Solution2:
    ___ findLongestChain(self, pairs: List[List[i..]]) __ i..:
        """
        Let F[i] be the longest chain   ended at A[i]
        F[i] = max(F[j] + 1 if predicate A[i] A[j])
        O(N^2)
        """
        pairs.s..(key=l.... x: t..(x))
        n = l..(pairs)
        F = [1 ___ _ __ r..(n)]
        ___ i __ r..(n):
            ___ j __ r..(i):
                __ pairs[j][1] < pairs[i][0]:
                    F[i] = max(F[i], F[j] + 1)

        r.. max(F)


__ _______ __ _______
    ... Solution().findLongestChain([[1,2], [2,3], [3,4]]) __ 2
