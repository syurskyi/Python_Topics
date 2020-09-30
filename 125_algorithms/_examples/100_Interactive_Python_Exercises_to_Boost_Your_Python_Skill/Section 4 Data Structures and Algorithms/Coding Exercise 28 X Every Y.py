import itertools

def foo(mylist, x, y):
    list_of_lists = [mylist[i:i+x] for i in range(0, len(mylist),y)]
    return list(itertools.chain.from_iterable(list_of_lists))