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


_______ c..


c_ Solution:
    ___ areSentencesSimilar  words1, words2, pairs
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        __ l..(words1) !_ l..(words2
            r.. F..

        simils c...d..(s..)

        ___ a, b __ pairs:
            simils[a].add(b)
            simils[b].add(a)

        ___ i __ r..(l..(words1:
            a words1[i]
            b words2[i]

            __ a !_ b a.. b n.. __ simils[a]:
                r.. F..

        r.. T..
