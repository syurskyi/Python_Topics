___ chain(dominoes
    __ le.(dominoes) __ 0:
        r_ []
    queue = [((dominoes[0],), tuple(dominoes[1:]))]
    w___ queue:
        chain, pool = queue.p..
        tail = chain[-1][-1] 
        __ chain[0][0] __ tail and le.(pool) __ 0:
            r_ chain
        ___ d, domino in enumerate(pool
            __ domino[0] != tail:
                domino = (domino[1], domino[0])
            __ domino[0] __ tail:
                queue.append((chain + (domino,), pool[:d] + pool[d+1:]))
