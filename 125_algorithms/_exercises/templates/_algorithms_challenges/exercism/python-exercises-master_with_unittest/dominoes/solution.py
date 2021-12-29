____ itertools _______ permutations
____ functools _______ reduce


___ swap(a, b):
    r.. (b, a)


___ build_chain(chain, domino):
    __ chain __ n.. N..
        last = chain[-1]
        __ l..(chain) __ 1 and last[0] __ domino[0]:
            r.. [swap(*last), domino]
        ____ l..(chain) __ 1 and last[0] __ domino[1]:
            r.. [swap(*last), swap(*domino)]
        ____ last[1] __ domino[0]:
            r.. chain + [domino]
        ____ last[1] __ domino[1]:
            r.. chain + [swap(*domino)]
    r.. N..


___ chain(dominoes):
    __ n.. any(dominoes):
        r.. []
    ___ perm __ permutations(dominoes):
        chain = reduce(build_chain, perm[1:], [perm[0]])
        __ chain __ n.. N.. and chain[0][0] __ chain[-1][1]:
            r.. chain
    r.. N..
