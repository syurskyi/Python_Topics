#!/usr/bin/python3
"""
We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is
the profit of the ith job.

Now we have some workers. worker[i] is the ability of the ith worker, which
means that this worker can only complete a job with difficulty at most worker[i].

Every worker can be assigned at most one job, but one job can be completed
multiple times.

For example, if 3 people attempt the same job that pays $1, then the total
profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get
profit of [20,20,30,30] seperately.
Notes:

1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
"""
____ t___ _______ L..


c_ Solution:
    ___ maxProfitAssignment  difficulty: L..[i..], profit: L..[i..], worker: L.. i.. __ i..
        """
        Greedy? Sort by profit
        """
        tasks l..(s..(z..(profit, difficulty)))
        worker.s..()
        i l..(tasks) - 1
        j l..(worker) - 1
        ret 0
        w.... i >_ 0 a.. j >_ 0:
            pro, diff tasks[i]
            __ worker[j] >_ diff:
                ret += pro
                j -_ 1
            ____
                i -_ 1

        r.. ret
