"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number
(floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
where equations.size() == values.size(), and the values are positive. This represents the equations. Return
vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

"""
____ c.. _______ defaultdict
____ i.. _______ izip

__author__ = 'Daniel'


c_ Solution(o..
    ___ calcEquation  equations, values, queries
        """
        transitive closure
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        G = defaultdict(d..)
        ___ edge, val __ izip(equations, values
            s, e = edge
            G[s][e], G[e][s] = val, 1/val
            G[s][s], G[e][e] = 1, 1

        r.. [dfs(G, s, e, s..()) ___ s, e __ queries]

    ___ dfs  G, s, e, path
        __ s n.. __ G o. e n.. __ G:
            r.. -1.0
        __ e __ G[s]:
            r.. G[s][e]
        ___ nbr __ G[s]:
            __ nbr n.. __ path:
                path.add(nbr)
                val = dfs(G, nbr, e, path)
                __ val != -1.0:
                    r.. val * G[s][nbr]
                path.remove(nbr)

        r.. -1.0


c_ Solution(o..
    ___ calcEquation  equations, values, queries
        """
        Floyd-Warshall algorithm
        transitive closure
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        G = defaultdict(d..)
        ___ edge, val __ izip(equations, values
            s, e = edge
            G[s][e], G[e][s] = val, 1/val
            G[s][s], G[e][e] = 1, 1

        # Floyd-Warshall
        ___ mid __ G:
            ___ s __ G[mid]:
                ___ e __ G[mid]:
                    G[s][e] = G[s][mid] * G[mid][e]

        r.. [G[s].get(e, -1.0) ___ s, e __ queries]

