#!/usr/bin/python3
"""
Given a char array representing tasks CPU need to do. It contains capital
letters A to Z where different letters represent different tasks. Tasks could be
done without original order. Each task could be done in one interval. For each
interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same
tasks, there must be at least n intervals that CPU are doing different tasks or
just be idle.

You need to return the least number of intervals the CPU will take to finish all
the given tasks.

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
from typing ______ List
from collections ______ deque, defaultdict
______ heapq


class Solution:
    ___ leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Gap is n

        Find the idle count

        use the max letter to construct page, # of page is max - 1
        (need also consider duplicate)

        Each page size is n + 1
        Free page size is n + 1 - (# of max)
        Find the idle count
        """
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1

        maxa = 0
        max_cnt = 0
        for v in counter.values(
            __ v > maxa:
                maxa = v
                max_cnt = 1
            ____ v __ maxa:
                max_cnt += 1

        page_cnt = maxa - 1
        free_page_size = n + 1 - max_cnt
        small_tasks = le.(tasks) - max_cnt * maxa
        idle = max(0, page_cnt * free_page_size - small_tasks)
        r_ le.(tasks) + idle


    ___ leastInterval_complicated(self, tasks: List[str], n: int) -> int:
        """
        greedy
        max heap, most tasks first
        cool down queue
        """
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1

        pq = [
            (-v, k)
            for k, v in counter.items()
        ]
        heapq.heapify(pq)
        q = deque()  # stores (t, k)
        clock = 0
        w___ pq or q:
            __ q and q[0][0] <= clock:
                # don't do w___ in w___ when clock++
                _, k = q.popleft()
                heapq.heappush(pq, (-counter[k], k))

            __ pq:
                _, k = heapq.heappop(pq)
                counter[k] -= 1
                __ counter[k] > 0:
                    q.append((clock + 1 + n, k))

            clock += 1

        r_ clock


__ __name__ __ "__main__":
    assert Solution().leastInterval(["A","A","A","B","B","B"], 0) __ 6
    assert Solution().leastInterval(["A","A","A","B","B","B"], 2) __ 8
