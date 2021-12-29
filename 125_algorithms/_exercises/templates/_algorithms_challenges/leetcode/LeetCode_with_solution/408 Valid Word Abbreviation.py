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
        while w < l..(word) and a < l..(abbr):
            __ abbr[a].isdigit() and abbr[a] != '0':
                e = a
                while e < l..(abbr) and abbr[e].isdigit(): e += 1
                num = int(abbr[a:e])
                a = e
                w += num
            ____:
                __ word[w] != abbr[a]:
                    r.. False

                w += 1
                a += 1

        r.. w __ l..(word) and a __ l..(abbr)


__ __name__ __ "__main__":
    ... Solution().validWordAbbreviation("internationalization", "i12iz4n") __ True
    ... Solution().validWordAbbreviation("apple", "a2e") __ False
