# network delay time - leetcode
class Solution:
    ___ networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        g = collections.defaultdict(list)
        ___ u, v, cost __ times:
            g[u].append((cost, v))

        # cost,node
        min_heap = [(0, K)]
        visited = set()
        distance = {i: float('inf') ___ i __ ra..(1, N+1)}
        distance[K] = 0

        w___ min_heap:
            cur_dist, u = heapq.heappop(min_heap)
            __ u __ visited:
                continue
            visited.add(u)
            __ le.(visited) __ N:
                r_ cur_dist

            ___ direct_distance, v __ g[u]:
                __ cur_dist + direct_distance < distance[v] and v not __ visited:
                    distance[v] = cur_dist + direct_distance
                    heapq.heappush(min_heap, (cur_dist + direct_distance, v))
        r_ -1
