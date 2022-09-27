c_ Solution o..
    ___ isAlienSorted  words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map  # dict
        ___ i, v __ e.. order):
            order_map[v] = i

        ___ cmp_alien(x, y):
            ls = min(l.. x), l.. y))
            index = 0
            w.. index < ls:
                __ x[index] != y[index]:
                    r_ order_map[x[index]] - order_map[y[index]]
                index += 1
            r_ l.. x) - l.. y)
        pos = 0
        w.. pos + 1 < l.. words):
            __ cmp_alien(words[pos], words[pos + 1]) > 0:
                r_ F..
            pos += 1
        r_ T..


__ ____ __ ____
    s  ?
    print s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    print s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
    print s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
