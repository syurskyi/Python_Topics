___ map_clone(function, xs
    r_ [function(elem) ___ elem in xs]


___ length(xs
    r_ su.(1 ___ _ in xs)


___ filter_clone(function, xs
    r_ [x ___ x in xs __ function(x)]


___ reverse(xs
    __ not xs:
        r_ []
    ____
        r_ xs[::-1]


___ append(xs, y
    xs[le.(xs] = [y]
    r_ xs


___ foldl(function, xs, acc
    __ le.(xs) __ 0:
        r_ acc
    ____
        r_ foldl(function, xs[1:], function(acc, xs[0]))


___ foldr(function, xs, acc
    __ le.(xs) __ 0:
        r_ acc
    ____
        r_ function(xs[0], foldr(function, xs[1:], acc))


___ flat(xs
    out = []
    ___ item in xs:
        __ isinstance(item, list
            out.extend(flat(item))
        ____
            out.append(item)
    r_ out


___ concat(xs, ys
    __ not ys:
        r_ xs
    ____
        ___ item in ys:
            xs.append(item)
        r_ xs
