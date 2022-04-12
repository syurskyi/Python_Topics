#!/usr/bin/python3
"""
There are 2N people a company is planning to interview. The cost of flying the
i-th person to city A is costs[i][0], and the cost of flying the i-th person to
city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people
arrive in each city.



Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
interviewing in each city.

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""


c_ Solution:
    ___ twoCitySchedCost  costs: L..[L..[i..]]) __ i..:
        """
        sort by city A and greedy? [30, 20]?
        sort by total?
        sort by diff - either choose A or B, the difference matters

        a - b: incremental cost of flying A instead of B
        """
        A [(a - b, a, b) ___ a, b __ costs]
        A.s..()
        ret 0
        remain l..(A) // 2
        ___ _, a, b __ A:
            __ remain > 0
                ret += a
                remain -_ 1
            ____
                ret += b

        r.. ret

    ___ twoCitySchedCost_error  costs: L..[L..[i..]]) __ i..:
        """
        sort by city A and greedy? [30, 20]?
        sort by total?
        sort by diff - either choose A or B, the difference matters

        Error in the abs of difference
        """
        A [(a..(a - b), a, b) ___ a, b __ costs]
        A.s..(r.._T..
        ret 0
        remain l..(A) // 2
        ___ _, a, b __ A:
            __ a > b:
                ret += b
            ____ remain > 0
                ret += a
                remain -_ 1
            ____
                ret += b

        r.. ret
