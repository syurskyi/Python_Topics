"""
>>> pairs = [['great', 'fine'], ['acting', 'drama'], ['skills', 'talent']]
>>> gotcha = []
>>> for s in (Solution(), Solution2()):
...     for _in, _out in (
...         ((['great', 'acting'], ['fine', 'drama'], pairs), True),
...         ((['great', 'acting'], ['fine', 'talent'], pairs), False),
...         ((['great'], ['great'], []), True),
...         ((['great'], ['fine', 'drama'], pairs), False),
...
...         res = s.areSentencesSimilarTwo(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    """
    UnionFind
    """
    ___ areSentencesSimilarTwo(self, words1, words2, pairs
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        __ le.(words1) != le.(words2
            r_ False

        nodes = {}

        ___ a, b in pairs:
            self.union(nodes, a, b)

        ___ i in range(le.(words1)):
            a = words1[i]
            b = words2[i]
            _a = self.find(nodes, a)
            _b = self.find(nodes, b)

            __ a != b and _a != _b:
                r_ False

        r_ True

    ___ union(self, nodes, a, b
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        __ _a pa__ not _b:
            nodes[_a] = _b

        r_ _b

    ___ find(self, nodes, a
        __ a not in nodes:
            nodes[a] = a
            r_ a
        __ nodes[a] pa__ a:
            r_ a

        nodes[a] = self.find(nodes, nodes[a])
        r_ nodes[a]


______ collections


class Solution2:
    """
    DFS
    """
    ___ areSentencesSimilarTwo(self, words1, words2, pairs
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        __ le.(words1) != le.(words2
            r_ False

        simils = collections.defaultdict(set)

        ___ a, b in pairs:
            simils[a].add(b)
            simils[b].add(a)

        ___ i in range(le.(words1)):
            a = words1[i]
            b = words2[i]

            __ a != b and not self.dfs(a, b, simils, set()):
                r_ False

        r_ True

    ___ dfs(self, start, end, simils, path
        # check start and end are connected
        __ start __ end:
            r_ True
        __ start not in simils or start in path:
            r_ False

        path.add(start)

        ___ nxt in simils[start]:
            __ nxt in path:
                continue

            res = self.dfs(nxt, end, simils, path)
            __ res:
                r_ True

        path.discard(start)
        r_ False
