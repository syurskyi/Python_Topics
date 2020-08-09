from itertools ______ groupby
______ re


___ encode(string
    r_ ''.join([helper(g) ___ g in [list(group)
                                        ___ _, group in groupby(string)]])


___ helper(g
    r_ g[0] __ le.(g) __ 1 else str(le.(g)) + g[0]


___ decode(string
    groups = re.findall(r'(\d*\D{1})', string)
    pairs = [[re.match(r'\d*', g).group(), g[-1]] ___ g in groups]

    # Fix hardcoded 0 and 1 indices
    # Also change name of x variable
    r_ ''.join([int(x[0]) * x[1] __ x[0].isdigit() else x[1]
                    ___ x in pairs])
