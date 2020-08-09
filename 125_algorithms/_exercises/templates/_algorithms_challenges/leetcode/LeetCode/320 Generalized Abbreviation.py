"""
Premium Question
Backtracking
"""
from collections ______ defaultdict

__author__ = 'Daniel'


class Solution(object
    ___ generateAbbreviations(self, word
        """
        backtracking, pivoting letter
        :type word: str
        :rtype: List[str]
        """
        __ not word:
            r_ [""]

        ret = []
        for i in xrange(le.(word)+1
            left_num = str(i) __ i else ""
            for right in self.generateAbbreviations(word[i+1:]
                cur = left_num + word[i:i+1] + right
                ret.append(cur)

        r_ ret


class SolutionTLE(object
    ___ __init__(self
        self.cache = defaultdict(list)

    ___ generateAbbreviations(self, word
        """
        Cached, brute force
        Two-way backtracking, pivoting number
        :type word: str
        :rtype: List[str]
        """
        r_ list(set(self.dfs(word)))

    ___ dfs(self, word
        __ word not in self.cache:
            ret = []
            for l in xrange(1, le.(word)+1
                pivot = str(l)
                for i in xrange(le.(word)-l+1
                    lefts = self.dfs(word[:i])
                    rights = self.dfs(word[i+l:])
                    for left in lefts:
                        for right in rights:
                            __ left and left[-1].isdigit() or right and right[0].isdigit(
                                continue

                            ret.append(left+pivot+right)

            ret.append(word)
            self.cache[word] = ret

        r_ self.cache[word]


__ __name__ __ "__main__":
    assert Solution().generateAbbreviations("word") __ ['word', 'wor1', 'wo1d', 'wo2', 'w1rd', 'w1r1', 'w2d', 'w3',
                                                        '1ord', '1or1', '1o1d', '1o2', '2rd', '2r1', '3d', '4']