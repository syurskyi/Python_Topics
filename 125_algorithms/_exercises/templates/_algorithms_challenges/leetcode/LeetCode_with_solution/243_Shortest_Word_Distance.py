c_ Solution o..
    # def shortestDistance(self, words, word1, word2):
    #     """
    #     :type words: List[str]
    #     :type word1: str
    #     :type word2: str
    #     :rtype: int
    #     """
    #     indexes = []
    #     for index, word in enumerate(words):
    #         if word1 == word:
    #             indexes.append((index, 1))
    #         elif word2 == word:
    #             indexes.append((index, 2))
    #     ls, min_range = len(indexes), len(words)
    #     for i in range(ls - 1):
    #         if indexes[i][1] == indexes[i + 1][1]:
    #             continue
    #         curr_range = abs(indexes[i][0] - indexes[i + 1][0])
    #         if curr_range < min_range:
    #             min_range = curr_range
    #     return min_range

    ___ shortestDistance  words, word1, word2
        index1 = index2 = -1
        res = l.. words)
        ___ index, word __ e.. words
            __ word1 __ word:
                index1 = index
            ____ word2 __ word:
                index2 = index
            __ index1 != -1 a.. index2 != -1:
                res = min(res, abs(index1 - index2))
        r_ res
