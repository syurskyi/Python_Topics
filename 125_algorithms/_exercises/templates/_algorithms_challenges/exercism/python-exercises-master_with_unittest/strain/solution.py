___ keep(seq, pred):
    res = []
    for el in seq:
        __ pred(el):
            res.append(el)
    return res


___ discard(seq, pred):
    res = []
    for el in seq:
        __ not pred(el):
            res.append(el)
    return res
