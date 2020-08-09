"""
>>> pairs = [['great', 'fine'], ['acting', 'drama'], ['skills', 'talent']]
>>> gotcha = []
>>> s = Solution()
>>> for _in, _out in (
...     ((['great', 'acting'], ['fine', 'drama'], pairs), True),
...     ((['great', 'acting'], ['fine', 'talent'], pairs), False),
...     ((['great'], ['great'], []), True),
...     ((['great'], ['fine', 'drama'], pairs), False),
...
...     res = s.areSentencesSimilar(*_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


______ collections


class Solution:
    ___ areSentencesSimilar(self, words1, words2, pairs
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

            __ a != b and b not in simils[a]:
                r_ False

        r_ True
