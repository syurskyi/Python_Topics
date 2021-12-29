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
____ typing _______ List
____ collections _______ defaultdict


class Solution:
    ___ numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        BFS
        bus based nodes rather than stop based nodes

        BFS = O(|V| + |E|) = O(N + N^2), where N is number of routes
        Construction = O (N^2 * S), where S is number of stops
        """
        __ S __ T:
            r.. 0

        routes = [set(e) ___ e __ routes]
        G = defaultdict(set)
        ___ i __ r..(l..(routes)):
            ___ j __ r..(i + 1, l..(routes)):
                stops_1, stops_2 = routes[i], routes[j]  # bus represented by stops
                ___ stop __ stops_1:  # any(stop in stops_2 for stop in stops_1)
                    __ stop __ stops_2:
                        G[i].add(j)
                        G[j].add(i)
                        break

        q = [i ___ i, stops __ e..(routes) __ S __ stops]
        target_set = set([i ___ i, stops __ e..(routes) __ T __ stops])
        visited = defaultdict(bool)
        ___ i __ q:
            visited[i] = True
        step = 1
        w.... q:
            cur_q    # list
            ___ e __ q:
                __ e __ target_set:
                    r.. step
                ___ nbr __ G[e]:
                    __ n.. visited[nbr]:
                        visited[nbr] = True
                        cur_q.a..(nbr)

            step += 1
            q = cur_q

        r.. -1

    ___ numBusesToDestination_TLE(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        BFS
        Lest number of buses rather than bus stops

        Connect stops within in bus use one edge in G
        """
        G = defaultdict(set)
        ___ stops __ routes:
            ___ i __ r..(l..(stops)):
                ___ j __ r..(i + 1, l..(stops)):
                    u, v = stops[i], stops[j]
                    G[u].add(v)
                    G[v].add(u)

        q = [S]
        step = 0
        visited = defaultdict(bool)
        visited[S] = True  # avoid add duplicate
        w.... q:
            cur_q    # list
            ___ e __ q:
                __ e __ T:
                    r.. step
                ___ nbr __ G[e]:
                    __ n.. visited[nbr]:
                        visited[nbr] = True
                        cur_q.a..(nbr)

            step += 1
            q = cur_q

        r.. -1


__ __name__ __ "__main__":
    ... Solution().numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) __ 2
