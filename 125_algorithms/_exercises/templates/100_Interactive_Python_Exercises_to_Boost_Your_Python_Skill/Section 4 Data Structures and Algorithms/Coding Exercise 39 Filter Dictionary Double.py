def foo(mydict):
    return dict((key, value) for key, value in mydict.items() if value > 4 and isinstance(value, int))