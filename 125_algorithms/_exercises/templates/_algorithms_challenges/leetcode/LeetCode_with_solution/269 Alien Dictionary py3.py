"""
There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of non-empty words from the
dictionary, where words are sorted lexicographically by the rules of this new
language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
"""
____ typing _______ List
____ collections _______ defaultdict, deque


class Solution(object):
    ___ alienOrder(self, words: List[str]) -> str:
        G = self.construct_graph(words)
        visited = defaultdict(int)  # 0 not visited, 1 visiting, 2 visted
        ret = deque()
        ___ u __ G.keys():
            __ visited[u] __ 0:
                __ n.. self.topo_dfs(G, u, visited, ret):
                    r.. ""

        r.. "".join(ret)

    ___ construct_graph(self, words):
        G = defaultdict(l..)
        # need to initialize, consider test case ["z", "z"]
        ___ w __ words:  # error
            ___ c __ w:
                G[c]

        ___ i __ r..(l..(words) - 1):  # compare word_i and word_{i+1}
            ___ c1, c2 __ zip(words[i], words[i+1]):
                __ c1 != c2:  # lexical order
                    G[c1].a..(c2)
                    break  # need to break for lexical order

        r.. G

    ___ topo_dfs(self, G, u, visited, ret):
        """
        Topological sort
        G = defaultdict(list)
        visited = defaultdict(int)  # 0 not visited, 1 visiteding, 2 visted

        pre-condition: u is not visited (0)
        """
        visited[u] = 1
        ___ nbr __ G[u]:
            __ visited[nbr] __ 1:
                r.. False
            __ visited[nbr] __ 0:
                __ n.. self.topo_dfs(G, nbr, visited, ret):
                    r.. False

        visited[u] = 2
        ret.appendleft(u)  # visit larger first
        r.. True


__ __name__ __ "__main__":
    lst = ["ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt", "ln", "ko", "jm", "il",
           "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"]
    ... Solution().alienOrder(lst) __ "zyxwvutsrqponmlkjihgfedcba"
