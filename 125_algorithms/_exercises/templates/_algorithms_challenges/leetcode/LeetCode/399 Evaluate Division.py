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
from collections ______ defaultdict
from itertools ______ izip

__author__ = 'Daniel'


class Solution(object
    ___ calcEquation(self, equations, values, queries
        """
        transitive closure
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        G = defaultdict(dict)
        ___ edge, val in izip(equations, values
            s, e = edge
            G[s][e], G[e][s] = val, 1/val
            G[s][s], G[e][e] = 1, 1

        r_ [self.dfs(G, s, e, set()) ___ s, e in queries]

    ___ dfs(self, G, s, e, path
        __ s not in G or e not in G:
            r_ -1.0
        __ e in G[s]:
            r_ G[s][e]
        ___ nbr in G[s]:
            __ nbr not in path:
                path.add(nbr)
                val = self.dfs(G, nbr, e, path)
                __ val != -1.0:
                    r_ val * G[s][nbr]
                path.remove(nbr)

        r_ -1.0


class Solution(object
    ___ calcEquation(self, equations, values, queries
        """
        Floyd-Warshall algorithm
        transitive closure
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        G = defaultdict(dict)
        ___ edge, val in izip(equations, values
            s, e = edge
            G[s][e], G[e][s] = val, 1/val
            G[s][s], G[e][e] = 1, 1

        # Floyd-Warshall
        ___ mid in G:
            ___ s in G[mid]:
                ___ e in G[mid]:
                    G[s][e] = G[s][mid] * G[mid][e]

        r_ [G[s].get(e, -1.0) ___ s, e in queries]

