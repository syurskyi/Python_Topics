from itertools import groupby
import re


___ encode(string):
    return ''.join([helper(g) for g in [list(group)
                                        for _, group in groupby(string)]])


___ helper(g):
    return g[0] __ len(g) == 1 else str(len(g)) + g[0]


___ decode(string):
    groups = re.findall(r'(\d*\D{1})', string)
    pairs = [[re.match(r'\d*', g).group(), g[-1]] for g in groups]

    # Fix hardcoded 0 and 1 indices
    # Also change name of x variable
    return ''.join([int(x[0]) * x[1] __ x[0].isdigit() else x[1]
                    for x in pairs])
