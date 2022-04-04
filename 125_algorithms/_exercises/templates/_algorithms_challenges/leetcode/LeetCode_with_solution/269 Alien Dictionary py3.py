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
____ c.. _______ d.., d..


c_ Solution(o..
    ___ alienOrder  words: List[s..]) __ s..:
        G = construct_graph(words)
        visited = d..(i..)  # 0 not visited, 1 visiting, 2 visted
        ret = d..()
        ___ u __ G.k..:
            __ visited[u] __ 0:
                __ n.. topo_dfs(G, u, visited, ret
                    r.. ""

        r.. "".j..(ret)

    ___ construct_graph  words
        G = d..(l..)
        # need to initialize, consider test case ["z", "z"]
        ___ w __ words:  # error
            ___ c __ w:
                G[c]

        ___ i __ r..(l..(words) - 1  # compare word_i and word_{i+1}
            ___ c1, c2 __ z..(words[i], words[i+1]
                __ c1 != c2:  # lexical order
                    G[c1].a..(c2)
                    _____  # need to break for lexical order

        r.. G

    ___ topo_dfs  G, u, visited, ret
        """
        Topological sort
        G = defaultdict(list)
        visited = defaultdict(int)  # 0 not visited, 1 visiteding, 2 visted

        pre-condition: u is not visited (0)
        """
        visited[u] = 1
        ___ nbr __ G[u]:
            __ visited[nbr] __ 1:
                r.. F..
            __ visited[nbr] __ 0:
                __ n.. topo_dfs(G, nbr, visited, ret
                    r.. F..

        visited[u] = 2
        ret.appendleft(u)  # visit larger first
        r.. T..


__ _______ __ _______
    lst = ["ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt", "ln", "ko", "jm", "il",
           "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"]
    ... Solution().alienOrder(lst) __ "zyxwvutsrqponmlkjihgfedcba"
