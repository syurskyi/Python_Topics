____ i.. _______ permutations
____ f.. _______ r..


___ swap(a, b
    r.. (b, a)


___ build_chain(c__, domino
    __ c__ __ n.. N..
        last c__[-1]
        __ l..(c__) __ 1 a.. last[0] __ domino[0]:
            r.. [swap(*last), domino]
        ____ l..(c__) __ 1 a.. last[0] __ domino[1]:
            r.. [swap(*last), swap(*domino)]
        ____ last[1] __ domino[0]:
            r.. c__ + [domino]
        ____ last[1] __ domino[1]:
            r.. c__ + [swap(*domino)]
    r.. N..


___ c__(dominoes
    __ n.. any(dominoes
        r.. []
    ___ perm __ p.. dominoes
        c__ r.. build_chain, perm[1:], [perm[0]])
        __ c__ __ n.. N.. a.. c__ 0 0  __ c__[-1][1]:
            r.. c__
    r.. N..
