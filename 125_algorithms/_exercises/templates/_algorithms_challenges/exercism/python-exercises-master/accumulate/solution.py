# [op(x) for x in seq] would be nice but trivial


___ accumulate(seq, op
    res = []
    ___ el in seq:
        res.append(op(el))
    r_ res
