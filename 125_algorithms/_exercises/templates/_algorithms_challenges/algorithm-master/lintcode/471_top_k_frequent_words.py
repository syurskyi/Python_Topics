c_ Solution:
    """
    @param: words: an array of string
    @param: k: An integer
    @return: an array of string
    """
    ___ topKFrequentWords  words, k
        __ n.. words o. n.. k:
            r.. []

        F    # dict
        ___ word __ words:
            F[word] = F.get(word, 0) + 1

        W = [(freq, word) ___ word, freq __ F.i..]
        W.s..(key=l.... item: (-item[0], item[1]))

        r.. [W[i][1] ___ i __ r..(k)]
