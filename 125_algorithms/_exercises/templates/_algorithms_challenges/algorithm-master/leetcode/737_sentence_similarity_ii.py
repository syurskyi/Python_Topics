"""
>>> pairs = [['great', 'fine'], ['acting', 'drama'], ['skills', 'talent']]
>>> gotcha = []
>>> for s in (Solution(), Solution2()):
...     for _in, _out in (
...         ((['great', 'acting'], ['fine', 'drama'], pairs), True),
...         ((['great', 'acting'], ['fine', 'talent'], pairs), False),
...         ((['great'], ['great'], []), True),
...         ((['great'], ['fine', 'drama'], pairs), False),
...     ):
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
    ___ areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        __ l..(words1) != l..(words2):
            r.. False

        nodes = {}

        ___ a, b __ pairs:
            self.union(nodes, a, b)

        ___ i __ r..(l..(words1)):
            a = words1[i]
            b = words2[i]
            _a = self.find(nodes, a)
            _b = self.find(nodes, b)

            __ a != b and _a != _b:
                r.. False

        r.. True

    ___ union(self, nodes, a, b):
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        __ _a __ n.. _b:
            nodes[_a] = _b

        r.. _b

    ___ find(self, nodes, a):
        __ a n.. __ nodes:
            nodes[a] = a
            r.. a
        __ nodes[a] __ a:
            r.. a

        nodes[a] = self.find(nodes, nodes[a])
        r.. nodes[a]


_______ collections


class Solution2:
    """
    DFS
    """
    ___ areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        __ l..(words1) != l..(words2):
            r.. False

        simils = collections.defaultdict(set)

        ___ a, b __ pairs:
            simils[a].add(b)
            simils[b].add(a)

        ___ i __ r..(l..(words1)):
            a = words1[i]
            b = words2[i]

            __ a != b and n.. self.dfs(a, b, simils, set()):
                r.. False

        r.. True

    ___ dfs(self, start, end, simils, path):
        # check start and end are connected
        __ start __ end:
            r.. True
        __ start n.. __ simils o. start __ path:
            r.. False

        path.add(start)

        ___ nxt __ simils[start]:
            __ nxt __ path:
                continue

            res = self.dfs(nxt, end, simils, path)
            __ res:
                r.. True

        path.discard(start)
        r.. False
