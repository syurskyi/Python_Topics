# network delay time - leetcode
c_ Solution:
    ___ networkDelayTime times: L..[L..[in.]], N: in., K: in.)  in.:

        g _ co...d_d_(list)
        ___ u, v, cost __ times:
            g[u].ap..((cost, v))

        # cost,node
        min_heap _ [(0, K)]
        visited _ set()
        distance _ {i: float('inf') ___ i __ ra..(1, N+1)}
        distance[K] _ 0

        w___ min_heap:
            cur_dist, u _ heapq.heappop(min_heap)
            __ u __ visited:
                continue
            visited.add(u)
            __ le.(visited) __ N:
                r_ cur_dist

            ___ direct_distance, v __ g[u]:
                __ cur_dist + direct_distance < distance[v] a.. v no. __ visited:
                    distance[v] _ cur_dist + direct_distance
                    heapq.heappush(min_heap, (cur_dist + direct_distance, v))
        r_ -1
