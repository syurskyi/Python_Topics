"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
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
                w.... e < l..(abbr) a.. abbr[e].isdigit(): e += 1
                num = int(abbr[a:e])
                a = e
                w += num
            ____:
                __ word[w] != abbr[a]:
                    r.. False

                w += 1
                a += 1

        r.. w __ l..(word) a.. a __ l..(abbr)


__ __name__ __ "__main__":
    ... Solution().validWordAbbreviation("internationalization", "i12iz4n") __ True
    ... Solution().validWordAbbreviation("apple", "a2e") __ False
