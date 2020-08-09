from itertools ______ groupby
from re ______ sub


___ decode(string
    r_ sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), string)


___ encode(string
    ___ single_helper(k, g
        l = le.(list(g))
        r_ k __ l __ 1 else str(l) + k
    r_ ''.join(single_helper(key, group) ___ key, group in groupby(string))
