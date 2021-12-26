def foo(mydict):
    lst = []
    for key, value in mydict.items():
        lst = lst + value
    return sum(lst)