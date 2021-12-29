"""
>>> pairs = [['great', 'fine'], ['acting', 'drama'], ['skills', 'talent']]
>>> gotcha = []
>>> s = Solution()
>>> for _in, _out in (
...     ((['great', 'acting'], ['fine', 'drama'], pairs), True),
...     ((['great', 'acting'], ['fine', 'talent'], pairs), False),
...     ((['great'], ['great'], []), True),
...     ((['great'], ['fine', 'drama'], pairs), False),
... ):
...     res = s.areSentencesSimilar(*_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


_______ collections


class Solution:
    ___ areSentencesSimilar(self, words1, words2, pairs):
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

            __ a != b a.. b n.. __ simils[a]:
                r.. False

        r.. True
