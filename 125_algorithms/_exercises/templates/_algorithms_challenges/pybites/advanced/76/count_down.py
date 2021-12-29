____ functools _______ singledispatch


@singledispatch
___ count_down(arg):
    __ n.. isi..(arg, (str, tuple, set,
                            int, float, d.., r..)):
        raise ValueError


@count_down.register(l..)
___ _(arg):
    ___ k __ r..(l..(arg)):
        print(''.join(map(str, arg)))
        arg.pop()


@count_down.register(str)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(r..)
___ _(arg):
    count_down(l..(arg))


@count_down.register(int)
@count_down.register(float)
___ _(arg):
    count_down(l..(str(arg)))


@count_down.register(d..)
___ _(arg):
    count_down(l..(arg.keys()))
