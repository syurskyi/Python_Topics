____ i.. _______ groupby
_______ __


___ encode(string):
    r.. ''.j..([helper(g) ___ g __ [l..(group)
                                        ___ _, group __ groupby(string)]])


___ helper(g):
    r.. g[0] __ l..(g) __ 1 ____ s..(l..(g)) + g[0]


___ decode(string):
    groups = __.f..(r'(\d*\D{1})', string)
    pairs = [[__.m..(r'\d*', g).group(), g[-1]] ___ g __ groups]

    # Fix hardcoded 0 and 1 indices
    # Also change name of x variable
    r.. ''.j..([i..(x[0]) * x[1] __ x[0].isdigit() ____ x[1]
                    ___ x __ pairs])
