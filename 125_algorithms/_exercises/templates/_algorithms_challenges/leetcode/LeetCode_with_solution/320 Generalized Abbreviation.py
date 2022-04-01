"""
Premium Question
Backtracking
"""
____ c.. _______ defaultdict

__author__ = 'Daniel'


c_ Solution(o..):
    ___ generateAbbreviations  word):
        """
        backtracking, pivoting letter
        :type word: str
        :rtype: List[str]
        """
        __ n.. word:
            r.. [""]

        ret    # list
        ___ i __ x..(l..(word)+1):
            left_num = s..(i) __ i ____ ""
            ___ right __ generateAbbreviations(word[i+1:]):
                cur = left_num + word[i:i+1] + right
                ret.a..(cur)

        r.. ret


c_ SolutionTLE(o..):
    ___ - ):
        cache = defaultdict(l..)

    ___ generateAbbreviations  word):
        """
        Cached, brute force
        Two-way backtracking, pivoting number
        :type word: str
        :rtype: List[str]
        """
        r.. l..(s..(dfs(word)))

    ___ dfs  word):
        __ word n.. __ cache:
            ret    # list
            ___ l __ x..(1, l..(word)+1):
                pivot = s..(l)
                ___ i __ x..(l..(word)-l+1):
                    lefts = dfs(word[:i])
                    rights = dfs(word[i+l:])
                    ___ left __ lefts:
                        ___ right __ rights:
                            __ left a.. left[-1].i.. o. right a.. right[0].i..
                                _____

                            ret.a..(left+pivot+right)

            ret.a..(word)
            cache[word] = ret

        r.. cache[word]


__ _______ __ _______
    ... Solution().generateAbbreviations("word") __ ['word', 'wor1', 'wo1d', 'wo2', 'w1rd', 'w1r1', 'w2d', 'w3',
                                                        '1ord', '1or1', '1o1d', '1o2', '2rd', '2r1', '3d', '4']