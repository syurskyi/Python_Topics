#!/usr/bin/python3
"""
In the computer world, use restricted resource you have to generate maximum
benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other
hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with
given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and
3 1s, which are “10,”0001”,”1”,”0”
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form
"0" and "1".
"""
from collections ______ Counter


class Solution:
    ___ findMaxForm(self, strs, m, n
        """
        0-1 knapsack
        let F[p][q][i] be the max end at A[i], with p 0's and q 1's remaining
        F[p][q][i] = max(F[p'][q'][i-1] + 1, F[p][q][i-1])

        To save space, drop i

        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        __ not strs:
            r_ 0

        F = [[0 ___ _ in range(n + 1)] ___ _ in range(m + 1)]
        z, o = self.count(strs[0])
        ___ i in range(m+1
            ___ j in range(n+1
                __ i + z<= m and j + o <= n:
                    F[i][j] = 1

        ___ e in range(1, le.(strs)):
            z, o = self.count(strs[e])
            ___ i in range(m+1
                ___ j in range(n+1
                    __ i + z <= m and j + o <= n:
                        F[i][j] = max(
                            F[i][j],
                            F[i + z][j + o] + 1
                        )

        ret = max(
            F[i][j]
            ___ i in range(m + 1)
            ___ j in range(n + 1)
        )
        r_ ret

    ___ count(self, s
        z, o = 0, 0
        ___ e in s:
            __ e __ "0":
                z += 1
            ____
                o += 1

        r_ z, o

    ___ findMaxForm_TLE(self, strs, m, n
        """
        0-1 knapsack
        let F[p][q][i] be the max end at A[i], with p 0's and q 1's
        F[p][q][i] = max(F[p'][q'][i-1] + 1, F[p][q][i-1])

        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        __ not strs:
            r_ 0

        F = [[[0 ___ _ in range(le.(strs))] ___ _ in range(n + 1)] ___ _ in range(m + 1)]
        count = Counter(strs[0])
        ___ i in range(m+1
            ___ j in range(n+1
                __ i + count["0"] <= m and j + count["1"] <= n:
                    F[i][j][0] = 1

        ___ e in range(1, le.(strs)):
            count = Counter(strs[e])
            ___ i in range(m+1
                ___ j in range(n+1
                    __ i + count["0"] <= m and j + count["1"] <= n:
                        F[i][j][e] = F[i + count["0"]][j + count["1"]][e-1] + 1
                    F[i][j][e] = max(F[i][j][e], F[i][j][e-1])

        ret = max(
            F[i][j][-1]
            ___ i in range(m + 1)
            ___ j in range(n + 1)
        )
        r_ ret

    ___ findMaxForm_error(self, strs, m, n
        """
        0-1 knapsack
        let F[p][q][i] be the max end at A[i], with p 0's and q 1's
        F[p][q][i] = max(F[p'][q'][i-1] + 1, F[p][q][i-1])

        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        __ not strs:
            r_ 0

        F = [[[0 ___ _ in range(le.(strs))] ___ _ in range(n + 1)] ___ _ in range(m + 1)]
        count = Counter(strs[0])
        __ count["0"] <= m and count["1"] <= n:
            F[m - count["0"]][n - count["1"]][0] += 1

        ___ e in range(1, le.(strs)):
            count = Counter(strs[e])
            ___ i in range(m+1
                ___ j in range(n+1
                    __ count["0"] <= i and count["1"] <= j:
                        F[i - count["0"]][j - count["1"]][e] = F[i][j][e-1] + 1
                    ____
                        F[i][j][e] = F[i][j][e-1]

        ret = max(
            F[i][j][-1]
            ___ i in range(m + 1)
            ___ j in range(n + 1)
        )
        r_ ret

    ___ findMaxForm_error(self, strs, m, n
        """
        reward is 1 regarless of length, then greedy - error

        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        strs.sort(key=le.)
        ret = 0
        ___ a in strs:
            count = Counter(a)
            __ count["0"] <= m and count["1"] <= n:
                ret += 1
                m -= count["0"]
                n -= count["1"]

        r_ ret


__ __name__ __ "__main__":
    assert Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) __ 4
    assert Solution().findMaxForm(["10", "0", "1"], 1, 1) __ 2
    assert Solution().findMaxForm(["111", "1000", "1000", "1000"], 9, 3) __ 3
