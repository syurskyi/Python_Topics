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
____ typing _______ List
____ collections _______ deque, defaultdict
_______ heapq


c_ Solution:
    ___ leastInterval(self, tasks: List[s..], n: int) -> int:
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
        ___ t __ tasks:
            counter[t] += 1

        maxa = 0
        max_cnt = 0
        ___ v __ counter.v..
            __ v > maxa:
                maxa = v
                max_cnt = 1
            ____ v __ maxa:
                max_cnt += 1

        page_cnt = maxa - 1
        free_page_size = n + 1 - max_cnt
        small_tasks = l..(tasks) - max_cnt * maxa
        idle = max(0, page_cnt * free_page_size - small_tasks)
        r.. l..(tasks) + idle


    ___ leastInterval_complicated(self, tasks: List[s..], n: int) -> int:
        """
        greedy
        max heap, most tasks first
        cool down queue
        """
        counter = defaultdict(int)
        ___ t __ tasks:
            counter[t] += 1

        pq = [
            (-v, k)
            ___ k, v __ counter.i..
        ]
        heapq.heapify(pq)
        q = deque()  # stores (t, k)
        clock = 0
        w.... pq o. q:
            __ q a.. q[0][0] <= clock:
                # don't do while in while when clock++
                _, k = q.popleft()
                heapq.heappush(pq, (-counter[k], k))

            __ pq:
                _, k = heapq.heappop(pq)
                counter[k] -= 1
                __ counter[k] > 0:
                    q.a..((clock + 1 + n, k))

            clock += 1

        r.. clock


__ __name__ __ "__main__":
    ... Solution().leastInterval(["A","A","A","B","B","B"], 0) __ 6
    ... Solution().leastInterval(["A","A","A","B","B","B"], 2) __ 8
