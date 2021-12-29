____ i.. _______ groupby
_______ re


___ encode(string):
    r.. ''.join([helper(g) ___ g __ [l..(group)
                                        ___ _, group __ groupby(string)]])


___ helper(g):
    r.. g[0] __ l..(g) __ 1 ____ s..(l..(g)) + g[0]


___ decode(string):
    groups = re.findall(r'(\d*\D{1})', string)
    pairs = [[re.match(r'\d*', g).group(), g[-1]] ___ g __ groups]

    # Fix hardcoded 0 and 1 indices
    # Also change name of x variable
    r.. ''.join([int(x[0]) * x[1] __ x[0].isdigit() ____ x[1]
                    ___ x __ pairs])
