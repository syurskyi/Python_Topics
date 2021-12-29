"""
Premium Question
Backtracking
"""
____ collections _______ defaultdict

__author__ = 'Daniel'


class Solution(object):
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
            left_num = str(i) __ i ____ ""
            ___ right __ self.generateAbbreviations(word[i+1:]):
                cur = left_num + word[i:i+1] + right
                ret.a..(cur)

        r.. ret


class SolutionTLE(object):
    ___ __init__(self):
        self.cache = defaultdict(l..)

    ___ generateAbbreviations(self, word):
        """
        Cached, brute force
        Two-way backtracking, pivoting number
        :type word: str
        :rtype: List[str]
        """
        r.. l..(set(self.dfs(word)))

    ___ dfs(self, word):
        __ word n.. __ self.cache:
            ret    # list
            ___ l __ xrange(1, l..(word)+1):
                pivot = str(l)
                ___ i __ xrange(l..(word)-l+1):
                    lefts = self.dfs(word[:i])
                    rights = self.dfs(word[i+l:])
                    ___ left __ lefts:
                        ___ right __ rights:
                            __ left and left[-1].isdigit() o. right and right[0].isdigit():
                                continue

                            ret.a..(left+pivot+right)

            ret.a..(word)
            self.cache[word] = ret

        r.. self.cache[word]


__ __name__ __ "__main__":
    ... Solution().generateAbbreviations("word") __ ['word', 'wor1', 'wo1d', 'wo2', 'w1rd', 'w1r1', 'w2d', 'w3',
                                                        '1ord', '1or1', '1o1d', '1o2', '2rd', '2r1', '3d', '4']