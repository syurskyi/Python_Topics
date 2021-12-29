from itertools import groupby
from re import sub


___ decode(string):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), string)


___ encode(string):
    ___ single_helper(k, g):
        l = len(list(g))
        return k __ l == 1 else str(l) + k
    return ''.join(single_helper(key, group) for key, group in groupby(string))
