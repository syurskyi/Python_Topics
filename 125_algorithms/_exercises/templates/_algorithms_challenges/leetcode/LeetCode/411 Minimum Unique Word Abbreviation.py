"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object
    ___ minAbbreviation(self, target, dictionary
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        ret = (target, le.(target))
        for abbr, abbr_l in self.dfs(target
            __ self.validate(dictionary, abbr) and ret[1] > abbr_l:
                ret = (abbr, abbr_l)

        r_ ret[0]

    ___ dfs(self, word
        """
        backtracking, pivoting letter
        :type word: str
        :rtype: List[str]
        """
        __ not word:
            r_ [("", 0)]

        ret = []
        for l in xrange(le.(word)+1
            left_num = str(l) __ l else ""
            left_l = 1 __ left_num != "" else 0
            left_l += 1 __ l < le.(word) else 0

            for right, right_l in self.dfs(word[l+1:]
                cur = left_num + word[l:l+1] + right  # word[l:l+1] possible ""
                ret.append((cur, left_l + right_l))

        r_ ret

    ___ validate(self, dictionary, abbr
        for w in dictionary:
            __ self.validWordAbbreviation(w, abbr
                r_ False

        r_ True

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
    assert Solution().minAbbreviation("apple", ["blade"]) __ "a4"
