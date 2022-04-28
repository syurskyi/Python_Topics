c_ Solution o..
    ___ validWordSquare  words):
        """
        :type words: List[str]
        :rtype: bool
        """
        __ words is N.. or l.. words) __ 0:
            r_ True
        ls = l.. words)
        ___ i __ r.. ls):
            ___ j __ r.. 1, l.. words[i])):
                __ j >= ls:
                    r_ False
                __ i >= l.. words[j]):
                    r_ False
                __ words[i][j] != words[j][i]:
                    r_ False
        r_ True

    # def validWordSquare(self, words):
    #     # https://discuss.leetcode.com/topic/63423/1-liner-python/2
    #     # The map(None, ...) transposes the "matrix", filling missing spots with None
    #     return map(None, *words) == map(None, *map(None, *words))
