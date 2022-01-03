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


c_ Solution:
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
            r.. F..

        nodes    # dict

        ___ a, b __ pairs:
            union(nodes, a, b)

        ___ i __ r..(l..(words1)):
            a = words1[i]
            b = words2[i]
            _a = find(nodes, a)
            _b = find(nodes, b)

            __ a != b a.. _a != _b:
                r.. F..

        r.. T..

    ___ union(self, nodes, a, b):
        _a = find(nodes, a)
        _b = find(nodes, b)

        __ _a __ n.. _b:
            nodes[_a] = _b

        r.. _b

    ___ find(self, nodes, a):
        __ a n.. __ nodes:
            nodes[a] = a
            r.. a
        __ nodes[a] __ a:
            r.. a

        nodes[a] = find(nodes, nodes[a])
        r.. nodes[a]


_______ collections


c_ Solution2:
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
            r.. F..

        simils = collections.defaultdict(set)

        ___ a, b __ pairs:
            simils[a].add(b)
            simils[b].add(a)

        ___ i __ r..(l..(words1)):
            a = words1[i]
            b = words2[i]

            __ a != b a.. n.. dfs(a, b, simils, set()):
                r.. F..

        r.. T..

    ___ dfs(self, start, end, simils, path):
        # check start and end are connected
        __ start __ end:
            r.. T..
        __ start n.. __ simils o. start __ path:
            r.. F..

        path.add(start)

        ___ nxt __ simils[start]:
            __ nxt __ path:
                continue

            res = dfs(nxt, end, simils, path)
            __ res:
                r.. T..

        path.discard(start)
        r.. F..
