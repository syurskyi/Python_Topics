from functools import singledispatch


@singledispatch
def count_down(arg):
    if not isinstance(arg, (str, tuple, set,
                            int, float, dict, range)):
        raise ValueError


@count_down.register(list)
def _(arg):
    for k in range(len(arg)):
        print(''.join(map(str, arg)))
        arg.pop()


@count_down.register(str)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(range)
def _(arg):
    count_down(list(arg))


@count_down.register(int)
@count_down.register(float)
def _(arg):
    count_down(list(str(arg)))


@count_down.register(dict)
def _(arg):
    count_down(list(arg.keys()))
