"""
Premium Question
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ validWordAbbreviation(self, word, abbr):
        """
        pointers
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        w = 0
        a = 0
        w.... w < l..(word) a.. a < l..(abbr):
            __ abbr[a].isdigit() a.. abbr[a] != '0':
                e = a
                w.... e < l..(abbr) a.. abbr[e].isdigit e += 1
                num = i..(abbr[a:e])
                a = e
                w += num
            ____:
                __ word[w] != abbr[a]:
                    r.. F..

                w += 1
                a += 1

        r.. w __ l..(word) a.. a __ l..(abbr)


__ _______ __ _______
    ... Solution().validWordAbbreviation("internationalization", "i12iz4n") __ T..
    ... Solution().validWordAbbreviation("apple", "a2e") __ F..
