#!/usr/bin/python3
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
____ c.. _______ d..

__author__ = 'Daniel'


c_ Solution(o..
    ___ alienOrder  words
        """
        :type words: List[str]
        :rtype: str
        """
        V = construct_graph(words)
        visited = s..()
        pathset = s..()
        ret    # list
        ___ v __ V.k..:
            __ v n.. __ visited:
                __ n.. topo_dfs(V, v, visited, pathset, ret
                    r.. ""

        r.. "".j..(r..(ret

    ___ construct_graph  words
        V = d..(l..)
        # need to initialize, consider test case ["z", "z"]
        ___ w __ words:  # pitfall
            ___ c __ w:
                V[c]
        ___ i __ x..(l..(words) - 1  # compare word_i and word_{i+1}
            ___ j __ x..(m..(l..(words[i]), l..(words[i+1]))):
                __ words[i][j] != words[i+1][j]:
                    V[words[i][j]].a..(words[i+1][j])
                    _____  # need to break for lexical order

        r.. V

    ___ topo_dfs  V, v, visited, pathset, ret
        """
        Topological sort
        :param V: Vertices HashMap
        :param v: currently visiting letter
        :param visited: visited letters
        :param pathset: marked predecessor in the path
        :param ret: the path, ordered  topologically
        :return: whether contains cycles
        """
        __ v __ pathset:
            r.. F..

        pathset.add(v)
        ___ nbr __ V[v]:
            __ nbr n.. __ visited:
                __ n.. topo_dfs(V, nbr, visited, pathset, ret
                    r.. F..

        pathset.remove(v)
        visited.add(v)  # add visited is in the end rather than at the begining
        ret.a..(v)  # append after lower values
        r.. T..

    ___ construct_graph_tedious  words, up, down, ptr, V
        """
        :param words:
        :param up: upper bound
        :param down: lower bound + 1
        :param ptr: starting index for the char in the word
        :param V: Vertices
        :return: None
        """
        i = up
        w.... i < down:
            __ ptr >_ l..(words[i]
                i += 1
            ____
                __ words[i][ptr] n.. __ V:
                    V[words[i][ptr]]    # list

                j = i+1
                w.... j < down a.. ptr < l..(words[j]) a.. words[j][ptr] __ words[i][ptr]:
                    j += 1

                construct_graph_tedious(words, i, j, ptr+1, V)
                __ j < down a.. ptr < l..(words[j]
                    V[words[i][ptr]].a..(words[j][ptr])

                i = j


__ _______ __ _______
    lst = ["ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt", "ln", "ko", "jm", "il",
           "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"]
    ... Solution().alienOrder(lst) __ "zyxwvutsrqponmlkjihgfedcba"
