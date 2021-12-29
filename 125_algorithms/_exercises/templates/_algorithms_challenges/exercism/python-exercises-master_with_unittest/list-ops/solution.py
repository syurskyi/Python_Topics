___ map_clone(function, xs):
    return [function(elem) for elem in xs]


___ length(xs):
    return sum(1 for _ in xs)


___ filter_clone(function, xs):
    return [x for x in xs __ function(x)]


___ reverse(xs):
    __ not xs:
        return []
    else:
        return xs[::-1]


___ append(xs, y):
    xs[len(xs):] = [y]
    return xs


___ foldl(function, xs, acc):
    __ len(xs) == 0:
        return acc
    else:
        return foldl(function, xs[1:], function(acc, xs[0]))


___ foldr(function, xs, acc):
    __ len(xs) == 0:
        return acc
    else:
        return function(xs[0], foldr(function, xs[1:], acc))


___ flat(xs):
    out = []
    for item in xs:
        __ isinstance(item, list):
            out.extend(flat(item))
        else:
            out.append(item)
    return out


___ concat(xs, ys):
    __ not ys:
        return xs
    else:
        for item in ys:
            xs.append(item)
        return xs
