import itertools

def foo(mylist):
    list_of_lists = [mylist[i:i+5] for i in range(0, len(mylist),7)]
    return list(itertools.chain.from_iterable(list_of_lists))
