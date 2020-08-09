#!/usr/bin/python3
"""
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus
repeats forever. For example if routes[0] = [1, 5, 7], this means that the first
bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop
T. Travelling by buses only, what is the least number of buses we must take to
reach our destination? Return -1 if it is not possible.

Example:
Input:
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation:
The best strategy is take the first bus to the bus stop 7, then take the second
bus to the bus stop 6.

Note:
1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.
"""
from typing ______ List
from collections ______ defaultdict


class Solution:
    ___ numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        BFS
        bus based nodes rather than stop based nodes

        BFS = O(|V| + |E|) = O(N + N^2), where N is number of routes
        Construction = O (N^2 * S), where S is number of stops
        """
        __ S __ T:
            r_ 0

        routes = [set(e) ___ e in routes]
        G = defaultdict(set)
        ___ i in range(le.(routes)):
            ___ j in range(i + 1, le.(routes)):
                stops_1, stops_2 = routes[i], routes[j]  # bus represented by stops
                ___ stop in stops_1:  # any(stop in stops_2 for stop in stops_1)
                    __ stop in stops_2:
                        G[i].add(j)
                        G[j].add(i)
                        break

        q = [i ___ i, stops in enumerate(routes) __ S in stops]
        target_set = set([i ___ i, stops in enumerate(routes) __ T in stops])
        visited = defaultdict(bool)
        ___ i in q:
            visited[i] = True
        step = 1
        w___ q:
            cur_q = []
            ___ e in q:
                __ e in target_set:
                    r_ step
                ___ nbr in G[e]:
                    __ not visited[nbr]:
                        visited[nbr] = True
                        cur_q.append(nbr)

            step += 1
            q = cur_q

        r_ -1

    ___ numBusesToDestination_TLE(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        BFS
        Lest number of buses rather than bus stops

        Connect stops within in bus use one edge in G
        """
        G = defaultdict(set)
        ___ stops in routes:
            ___ i in range(le.(stops)):
                ___ j in range(i + 1, le.(stops)):
                    u, v = stops[i], stops[j]
                    G[u].add(v)
                    G[v].add(u)

        q = [S]
        step = 0
        visited = defaultdict(bool)
        visited[S] = True  # avoid add duplicate
        w___ q:
            cur_q = []
            ___ e in q:
                __ e __ T:
                    r_ step
                ___ nbr in G[e]:
                    __ not visited[nbr]:
                        visited[nbr] = True
                        cur_q.append(nbr)

            step += 1
            q = cur_q

        r_ -1


__ __name__ __ "__main__":
    assert Solution().numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) __ 2
