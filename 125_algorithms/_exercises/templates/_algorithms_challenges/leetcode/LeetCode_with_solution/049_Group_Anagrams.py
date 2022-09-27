c_ Solution o..
    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     hash = {}
    #     for s in strs:
    #         key = self.hash_key(s)
    #         try:
    #             hash[key].append(s)
    #         except KeyError:
    #             hash[key] = [s]
    #     for k, v in hash.items():
    #         if len(v) > 1:
    #             # sort
    #             v.sort()
    #     return hash.values()
    #
    # def hash_key(self, s):
    #     # hash string with 26 length array
    #     table = [0] * 26
    #     for ch in s:
    #         index = ord(ch) - ord('a')
    #         table[index] += 1
    #     return str(table)

    ___ groupAnagrams  strs):
        strs.s..
        hash  # dict
        ___ s __ strs:
            key = hash_key(s)
            try:
                hash[key].append(s)
            except KeyError:
                hash[key] = [s]
        r_ hash.values()

    ___ hash_key  s):
        # hash string with 26 length array
        table = [0] * 26
        ___ ch __ s:
            index = o.. ch) - o.. 'a')
            table[index] += 1
        r_ s..(table)