___ keep(seq, pred
    res = []
    ___ el in seq:
        __ pred(el
            res.append(el)
    r_ res


___ discard(seq, pred
    res = []
    ___ el in seq:
        __ not pred(el
            res.append(el)
    r_ res
