#!/usr/bin/python3
"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w),
where u is the source node, v is the target node, and w is the time it takes for
a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes
to receive the signal? If it is impossible, return -1.

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""
____ typing _______ List
____ collections _______ defaultdict
_______ heapq


class Solution:
    ___ networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        Dijkstra's algorithm
        """
        G = defaultdict(d..)
        reach_time = [float('inf') ___ _ __ r..(N + 1)]
        ___ u, v, w __ times:
            G[u][v] = w

        h = [(0, K)]
        reach_time[K] = 0
        while h:
            t, s = heapq.heappop(h)
            __ s __ G:
                ___ d, w __ G[s].items():
                    __ t + w < reach_time[d]:
                        reach_time[d] = t + w
                        heapq.heappush(h, (t + w, d))

        ret = max(reach_time[1:])  # notice reach_time[0] is dummy
        __ ret __ float('inf'):
            r.. -1
        r.. ret


__ __name__ __ "__main__":
    ... Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) __ 2
