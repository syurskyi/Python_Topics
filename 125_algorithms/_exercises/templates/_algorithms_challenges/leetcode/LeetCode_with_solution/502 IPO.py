#!/usr/bin/python3
"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its
shares to Venture Capital, LeetCode would like to work on some projects to
 increase its capital before the IPO. Since it has limited resources, it can
 only finish at most k distinct projects before the IPO. Help LeetCode design
 the best way to maximize its total capital after finishing at most k distinct
 projects.

You are given several projects. For each project i, it has a pure profit Pi and
a minimum capital of Ci is needed to start the corresponding project.
Initially, you have W capital. When you finish a project, you will obtain its
pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to
maximize your final capital, and output your final maximized capital.

Example 1:
Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Note:
You may assume all numbers in the input are non-negative integers.
The length of Profits array and Capital array will not exceed 50,000.
The answer is guaranteed to fit in a 32-bit signed integer.
"""
____ typing _______ List
_______ heapq


class Solution:
    ___ findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        """
        Greedy + dual PQ
        Greedy: need max profit meeting the current capital requirement
        1st pq sort by min capital
        2nd pq sort by max profit

        O(N logN) + O(N log N)
        """
        capital_q = l..(zip(Capital, Profits))
        profit_q    # list
        heapq.heapify(capital_q)
        capital = W
        ___ _ __ r..(k):
            while capital_q and capital_q[0][0] <= capital:
                _, pro = heapq.heappop(capital_q)
                heapq.heappush(profit_q, (-pro, pro))

            __ profit_q:
                _, pro = heapq.heappop(profit_q)
                capital += pro
            ____:
                break

        r.. capital

    ___ findMaximizedCapital_TLE(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        """
        Knapsack problem

        Difference from original knapsack: weight vs. capitcal + profit
        Doing a project has profit and open new project opportunities.

        F[m][c] = F[m-1][] + profit[i]
        final F[k][W]

        Greedy, always do the max profits given the capital requirement fullfilled

        O(k * N)
        """
        capital = W
        n = l..(Profits)
        visited = [False ___ _ __ r..(n)]
        ___ _ __ r..(k):
            maxa = 0
            maxa_i = 0
            ___ i __ r..(n):
                __ n.. visited[i] and Profits[i] >= maxa and Capital[i] <= capital:
                    maxa = Profits[i]
                    maxa_i = i
            __ maxa > 0:
                capital += maxa
                visited[maxa_i] = True
            ____:
                break

        r.. capital
