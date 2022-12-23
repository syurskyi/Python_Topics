c_ Solution o..
    ___ palindromePairs  words
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # https://leetcode.com/problems/palindrome-pairs/discuss/79219/Python-solution~
        # reverse word and create a word to index map
        word2index, res = dict([(w||-1], i) ___ i, w __ e.. words)]),    # list
        ___ i, word __ e.. words
            ___ j __ xrange(l.. word) + 1
                # Use prefix and postfix
                # rather than going through all posible combinations
                prefix, postfix = word[:j], word[j:]
                # prefix + postfix + reverse(prfix)
                __ prefix __ word2index a.. i != word2index[prefix] a.. postfix __ postfix||-1]:
                    res.a.. [i, word2index[prefix]])
                # reverse(postfix) + prefix + postfix
                __ j > 0 a.. postfix __ word2index a.. i != word2index[postfix] a.. prefix __ prefix||-1]:
                    res.a.. [word2index[postfix], i])
        r_ res
