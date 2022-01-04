"""
Premium Question
"""
__author__ = 'Daniel'


c_ Solution(object):
    ___ minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        ret = (target, l..(target))
        ___ abbr, abbr_l __ dfs(target):
            __ validate(dictionary, abbr) a.. ret[1] > abbr_l:
                ret = (abbr, abbr_l)

        r.. ret[0]

    ___ dfs(self, word):
        """
        backtracking, pivoting letter
        :type word: str
        :rtype: List[str]
        """
        __ n.. word:
            r.. [("", 0)]

        ret    # list
        ___ l __ xrange(l..(word)+1):
            left_num = s..(l) __ l ____ ""
            left_l = 1 __ left_num != "" ____ 0
            left_l += 1 __ l < l..(word) ____ 0

            ___ right, right_l __ dfs(word[l+1:]):
                cur = left_num + word[l:l+1] + right  # word[l:l+1] possible ""
                ret.a..((cur, left_l + right_l))

        r.. ret

    ___ validate(self, dictionary, abbr):
        ___ w __ dictionary:
            __ validWordAbbreviation(w, abbr):
                r.. F..

        r.. T..

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
    ... Solution().minAbbreviation("apple", ["blade"]) __ "a4"
