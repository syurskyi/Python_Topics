"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this
subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
"""
____ c.. _______ d..

__author__ 'Daniel'


c_ Solution(o..
    ___ largestDivisibleSubset  A
        """
        Given a divisible subset, when adding a new number, we only needs to validate whether the new number is
        divisible by the largest number in the divisible subset.

        Let F[i] for the size of subset ended with A[i]
        F[i] = max(1 + F[j] if A[i] % A[j] == 0 for j in xrange(i-1))
        pi[i] = argmax(...)
        :type A: List[int]
        :rtype: List[int]
        """
        __ n.. A: r.. []

        F    # dict
        pi    # dict
        A.s..()
        ___ i __ x..(l..(A:
            F[i] 1
            pi[i] i
            ___ j __ x..(i
                __ A[i] % A[j] __ 0:
                    __ F[i] < 1 + F[j]:
                        F[i] 1 + F[j]
                        pi[i] j

        max_i, max_v 0, 1
        ___ k, v __ F.i..:
            __ v > max_v:
                max_i, max_v k, v

        ret d..()
        cur max_i
        ret.appendleft(A[cur])
        w.... pi[cur] !_ cur:
            cur pi[cur]
            ret.appendleft(A[cur])

        r.. l..(ret)


__ _______ __ _______
    ... Solution().largestDivisibleSubset([1, 2, 4, 8]) __ [1, 2, 4, 8]
