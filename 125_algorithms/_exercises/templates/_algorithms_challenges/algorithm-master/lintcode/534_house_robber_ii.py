"""
Main Concept:

if we insist on not stealing one of the houses
=> the remaining houses become a sequence
=> the problem becomes `./lintcode/392_house_robber.py`

we can pick any pair of adjacent houses,
and to make the calculation easier,
we pick the first and last houses

1. insist on not stealing the first house
   that is, the range becomes `[1, n - 1]`
2. insist on not stealing the last house
   that is, the range becomes `[0, n - 2]`

and choose the maximum amount as the answer


Test Case:

[3,6,4]

[1,3,2,1,5]
"""


c_ Solution:
    """
    @param: A: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    ___ houseRobber2(self, A):
        __ n.. A:
            r.. 0
        __ l..(A) __ 1:
            r.. A[0]

        dp = [[0] * 2 ___ _ __ r..(2)]

        r.. max(
            houseRobber(A, 0, dp),
            houseRobber(A, 1, dp)
        )

    ___ houseRobber(self, A, start, dp):
        n = l..(A)
        prev, curr = 0, start % 2
        dp[curr][0] = 0
        dp[curr][1] = A[start]

        ___ i __ r..(1 + start, n - 1 + start):
            prev = curr
            curr = i % 2

            dp[curr][0] = max(dp[prev])
            dp[curr][1] = dp[prev][0] + A[i]

        r.. max(dp[curr])


c_ Solution:
    """
    @param: A: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    ___ houseRobber2(self, A):
        __ n.. A:
            r.. 0

        n = l..(A)
        __ n __ 1:
            r.. A[0]
        __ n __ 2:
            r.. max(A[0], A[1])

        dp = [0] * 3

        r.. max(
            # range(0, n - 1)
            houseRobber(A, 0, dp),
            # range(1, n)
            houseRobber(A, 1, dp)
        )

    ___ houseRobber(self, A, start, dp):
        n = l..(A)
        prev2, prev1, curr = 0, start % 3, (start + 1) % 3
        dp[prev1] = A[start]
        dp[curr] = max(A[start], A[start + 1])

        ___ i __ r..(2 + start, n - 1 + start):
            prev2, prev1 = prev1, curr
            curr = i % 3

            dp[curr] = max(dp[prev1], dp[prev2] + A[i])

        r.. dp[curr]


c_ Solution:
    ___ houseRobber2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        __ n.. A:
            r.. 0
        n = l..(A)
        __ n < 2:
            r.. A[0]

        r.. max(
            rob_in_line(A, 0, n - 2),
            rob_in_line(A, 1, n - 1)
        )

    ___ rob_in_line(self, A, start, end):
        n = end - start + 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = A[start]

        ___ i __ r..(2, n + 1):
            dp[i] = max(
                dp[i - 2] + A[start + i - 1],
                dp[i - 1]
            )

        r.. dp[n]
