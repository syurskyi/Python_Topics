#!/usr/bin/python3
"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned
(0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find
minimum cost to reach the top of the floor, and you can either start from the
step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping
cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""
____ t___ _______ L..


c_ Solution:
    ___ minCostClimbingStairs  cost: L.. i.. __ i..
        """
        dp
        let F[i] be the cost to reach i-th stair
        F[i] = min
            F[i-2] + cost[i-2]
            F[i-1] + cost[i-1]
        """
        n l..(cost)
        F [f__('inf') ___ _ __ r..(n+1)]
        F[0] 0
        F[1] 0
        ___ i __ r..(2, n+1
            F[i] m..(
                F[i-2] + cost[i-2],
                F[i-1] + cost[i-1]
            )

        r.. F[-1]


__ _______ __ _______
    ... Solution().minCostClimbingStairs([10, 15, 20]) __ 15
