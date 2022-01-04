"""
Premium Question
Backtracking
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


c_ Solution(object):
    ___ generateAbbreviations(self, word):
        """
        backtracking, pivoting letter
        :type word: str
        :rtype: List[str]
        """
        __ n.. word:
            r.. [""]

        ret    # list
        ___ i __ xrange(l..(word)+1):
            left_num = s..(i) __ i ____ ""
            ___ right __ generateAbbreviations(word[i+1:]):
                cur = left_num + word[i:i+1] + right
                ret.a..(cur)

        r.. ret


c_ SolutionTLE(object):
    ___ - ):
        cache = defaultdict(l..)

    ___ generateAbbreviations(self, word):
        """
        Cached, brute force
        Two-way backtracking, pivoting number
        :type word: str
        :rtype: List[str]
        """
        r.. l..(set(dfs(word)))

    ___ dfs(self, word):
        __ word n.. __ cache:
            ret    # list
            ___ l __ xrange(1, l..(word)+1):
                pivot = s..(l)
                ___ i __ xrange(l..(word)-l+1):
                    lefts = dfs(word[:i])
                    rights = dfs(word[i+l:])
                    ___ left __ lefts:
                        ___ right __ rights:
                            __ left a.. left[-1].isdigit() o. right a.. right[0].isdigit
                                continue

                            ret.a..(left+pivot+right)

            ret.a..(word)
            cache[word] = ret

        r.. cache[word]


__ __name__ __ "__main__":
    ... Solution().generateAbbreviations("word") __ ['word', 'wor1', 'wo1d', 'wo2', 'w1rd', 'w1r1', 'w2d', 'w3',
                                                        '1ord', '1or1', '1o1d', '1o2', '2rd', '2r1', '3d', '4']