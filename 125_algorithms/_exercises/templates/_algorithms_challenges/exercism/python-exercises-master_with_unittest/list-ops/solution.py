___ map_clone(function, xs
    r.. [function(elem) ___ elem __ xs]


___ length(xs
    r.. s..(1 ___ _ __ xs)


___ filter_clone(function, xs
    r.. [x ___ x __ xs __ function(x)]


___ reverse(xs
    __ n.. xs:
        r.. []
    ____
        r.. xs[::-1]


___ a..(xs, y
    xs[l..(xs] [y]
    r.. xs


___ foldl(function, xs, acc
    __ l..(xs) __ 0:
        r.. acc
    ____
        r.. foldl(function, xs[1:], function(acc, xs[0]


___ foldr(function, xs, acc
    __ l..(xs) __ 0:
        r.. acc
    ____
        r.. function(xs[0], foldr(function, xs[1:], acc


___ flat(xs
    out    # list
    ___ item __ xs:
        __ isi..(item, l..
            out.e.. flat(item
        ____
            out.a..(item)
    r.. out


___ concat(xs, ys
    __ n.. ys:
        r.. xs
    ____
        ___ item __ ys:
            xs.a..(item)
        r.. xs
