def foo(lst, item):
    if len(lst) == 3:
        lst.pop(0)
        lst.append(item)
        return lst