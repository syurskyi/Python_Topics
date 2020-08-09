___ flatten(list_of_lists
    res = []
    for i in list_of_lists:
        __ isinstance(i, (list, tuple)):
            res.extend(flatten(i))
        ____
            res.append(i)
    r_ res
