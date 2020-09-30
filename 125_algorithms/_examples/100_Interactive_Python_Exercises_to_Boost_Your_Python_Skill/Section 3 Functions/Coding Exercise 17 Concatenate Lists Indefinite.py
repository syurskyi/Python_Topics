def foo(*args):
    lst = []
    for eachlist in args:
        lst = lst + eachlist
    return lst