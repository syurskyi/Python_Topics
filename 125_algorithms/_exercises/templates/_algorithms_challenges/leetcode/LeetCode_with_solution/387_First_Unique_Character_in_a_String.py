c_ Solution o..
    ___ firstUniqChar  s):
        """
        :type s: str
        :rtype: int
        """
        count_map  # dict
        ___ c __ s:
            count_map[c] = count_map.get(c, 0) + 1
        ___ i, c __ e.. s):
            __ count_map[c] __ 1:
                r_ i
        r_ -1

    # def firstUniqChar(self, s):
    #     min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])
