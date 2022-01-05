#!/usr/bin/python3
"""
Given an integer array A, and an integer target, return the number of tuples
i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Note:

3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""
____ typing _______ List
____ c.. _______ defaultdict


MOD = 10 ** 9 + 7


c_ Solution:
    ___ threeSumMulti  A: List[i..], target: i..) __ i..:
        """
        Adapted from 3 sum
        3 pointers O(N + K^2)
        j, k scan each element once
        """
        counter = defaultdict(i..)
        ___ a __ A:
            counter[a] += 1

        keys = l..(counter.keys())
        keys.s..()
        n = l..(keys)
        ret = 0
        ___ i __ r..(n):
            j = i  # not i + 1
            k = n - 1
            w.... j <= k:  # not <
                a, b, c = keys[i], keys[j], keys[k]
                __ b + c < target - a:
                    j += 1
                ____ b + c > target - a:
                    k -= 1
                ____:  # equal
                    __ a < b < c:
                        ret += counter[a] * counter[b] * counter[c]
                    ____ a __ b < c:
                        # nC2
                        ret += counter[a] * (counter[a] - 1) // 2 * counter[c]
                    ____ a < b __ c:
                        ret += counter[a] * counter[b]  * (counter[b] - 1) // 2
                    ____ a__ b __ c:
                        # nC3
                        ret += counter[a] * (counter[a] - 1) * (counter[a] - 2) // (3 * 2)
                    ____:
                        r..

                    ret %= MOD
                    j += 1
                    k -= 1

        r.. ret

    ___ threeSumMulti_TLE  A: List[i..], target: i..) __ i..:
        """
        Adapted from 3 sum
        3 pointers O(N^2)
        j, k scan each element once
        """
        A.s..()
        n = l..(A)
        ret = 0
        ___ i __ r..(n):
            j = i + 1
            k = n - 1
            w.... j < k:
                __ A[j] + A[k] < target - A[i]:
                    j += 1
                ____ A[j] + A[k] > target - A[i]:
                    k -= 1
                ____:  # equal
                    l_cnt = 1
                    w.... j + l_cnt < n a.. A[j + l_cnt] __ A[j]:
                        l_cnt += 1

                    r_cnt = 1
                    w.... k - r_cnt >= 0 a.. A[k - r_cnt] __ A[k]:
                        r_cnt += 1

                    __ A[j] != A[k]:
                        ret += l_cnt * r_cnt
                        ret %= MOD
                    ____:
                        ret += l_cnt * (l_cnt - 1) // 2  # nC2
                        ret %= MOD

                    j += l_cnt
                    k -= r_cnt

        r.. ret

    ___ threeSumMulti_TLE  A: List[i..], target: i..) __ i..:
        """
        O(n * target * 3)
        Let F[i][t][k] be the number of k sums using A[:i] to target t
        """
        n = l..(A)
        F = [[[0 ___ _ __ r..(3 + 1)] ___ _ __ r..(target + 1)] ___ _ __ r..(n+1)]

        ___ i __ r..(n+1):
            F[i][0][0] = 1

        ___ i __ r..(1, n + 1):
            ___ t __ r..(target + 1):
                ___ k __ r..(1, 3 + 1):
                    # choose A[i-1] or not
                    F[i][t][k] = F[i-1][t][k] % MOD
                    __ t - A[i-1] >= 0:
                        F[i][t][k] += F[i-1][t-A[i-1]][k-1] % MOD

        print(F[n][target][3])
        r.. F[n][target][3]

    ___ threeSumMulti_TLE  A: List[i..], target: i..) __ i..:
        """
        O(n * target * 3)
        Let F[i][t][k] be the number of k sums using A[:i] to target t
        """
        F = defaultdict(l....: defaultdict(l....: defaultdict(i..)))
        n = l..(A)
        ___ i __ r..(n+1):
            F[i][0][0] = 1

        ___ i __ r..(1, n + 1):
            ___ t __ r..(target + 1):
                ___ k __ r..(1, 3 + 1):
                    # choose A[i-1] or not
                    F[i][t][k] = F[i-1][t][k] + F[i-1][t-A[i-1]][k-1]
                    F[i][t][k] %= MOD

        r.. F[n][target][3]


__ _______ __ _______
    ... Solution().threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8) __ 20
