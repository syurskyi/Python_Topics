from itertools ______ permutations
from functools ______ reduce


___ swap(a, b
    r_ (b, a)


___ build_chain(chain, domino
    __ chain is not None:
        last = chain[-1]
        __ le.(chain) __ 1 and last[0] __ domino[0]:
            r_ [swap(*last), domino]
        ____ le.(chain) __ 1 and last[0] __ domino[1]:
            r_ [swap(*last), swap(*domino)]
        ____ last[1] __ domino[0]:
            r_ chain + [domino]
        ____ last[1] __ domino[1]:
            r_ chain + [swap(*domino)]
    r_ None


___ chain(dominoes
    __ not any(dominoes
        r_ []
    ___ perm in permutations(dominoes
        chain = reduce(build_chain, perm[1:], [perm[0]])
        __ chain is not None and chain[0][0] __ chain[-1][1]:
            r_ chain
    r_ None
