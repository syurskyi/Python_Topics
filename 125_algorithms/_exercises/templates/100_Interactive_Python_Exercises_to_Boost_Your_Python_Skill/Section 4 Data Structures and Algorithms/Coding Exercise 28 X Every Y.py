import itertools

___ foo(mylist, x, y):
    list_of_lists = [mylist[i:i+x] ___ i __ range(0, len(mylist),y)]
    r_ list(itertools.chain.from_iterable(list_of_lists))