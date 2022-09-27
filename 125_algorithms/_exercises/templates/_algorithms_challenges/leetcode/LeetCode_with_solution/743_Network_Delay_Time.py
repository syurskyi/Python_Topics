c_ Solution o..
    # def networkDelayTime(self, times, N, K):
    #     # DFS
    #     graph = collections.defaultdict(list)
    #     for u, v, w in times:
    #         graph[u].append((w, v))

    #     dist = {node: float('inf') for node in xrange(1, N + 1)}

    #     def dfs(node, elapsed):
    #         if elapsed >= dist[node]: return
    #         dist[node] = elapsed
    #         for time, nei in sorted(graph[node]):
    #             dfs(nei, elapsed + time)

    #     dfs(K, 0)
    #     ans = max(dist.values())
    #     return ans if ans < float('inf') else -1

    ___ networkDelayTime  times, N, K):
        # Dijkstra
        graph = collections.defaultdict(list)
        ___ u, v, w __ times:
            graph[u].append((v, w))

        dist = {node: float('inf') ___ node __ xrange(1, N + 1)}
        seen = [F..] * (N + 1)
        dist[K] = 0

        w.. T..:
            cand_node = -1
            cand_dist = float('inf')
            ___ i __ xrange(1, N + 1):
                __ not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            __ cand_node < 0: break
            seen[cand_node] = T..
            ___ nei, d __ graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        r_ ans __ ans < float('inf') ____ -1
