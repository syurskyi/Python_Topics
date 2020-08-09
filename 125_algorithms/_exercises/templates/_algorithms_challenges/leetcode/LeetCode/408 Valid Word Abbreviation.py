"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object
    ___ validWordAbbreviation(self, word, abbr
        """
        pointers
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        w = 0
        a = 0
        w___ w < le.(word) and a < le.(abbr
            __ abbr[a].isdigit() and abbr[a] != '0':
                e = a
                w___ e < le.(abbr) and abbr[e].isdigit( e += 1
                num = int(abbr[a:e])
                a = e
                w += num
            ____
                __ word[w] != abbr[a]:
                    r_ False

                w += 1
                a += 1

        r_ w __ le.(word) and a __ le.(abbr)


__ __name__ __ "__main__":
    assert Solution().validWordAbbreviation("internationalization", "i12iz4n") __ True
    assert Solution().validWordAbbreviation("apple", "a2e") __ False
