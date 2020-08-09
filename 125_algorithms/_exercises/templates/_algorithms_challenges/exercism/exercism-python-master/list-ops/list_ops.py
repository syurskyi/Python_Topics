___ append(xs, ys
    r_ concat([xs, ys])


___ concat(lists
    r_ [item for lst in lists for item in lst]


___ filter_clone(function, xs
    r_ [x for x in xs __ function(x)]


___ length(xs
    result = 0
    for _ in xs:
        result += 1
    r_ result


___ map_clone(function, xs
    r_ [function(x) for x in xs]


___ foldl(function, xs, acc
    for x in xs:
        acc = function(acc, x)
    r_ acc

___ foldr(function, xs, acc
    r_ foldl(lambda x, acc: function(acc, x), reverse(xs), acc)


___ reverse(xs
    r_ foldl(lambda acc, x: append([x], acc), xs, [])
