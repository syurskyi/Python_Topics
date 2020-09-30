___ flatten(list_of_lists
    res =   # list
    ___ i __ list_of_lists:
        __ isinstance(i, (list, tu..)):
            res.extend(flatten(i))
        ____
            res.append(i)
    r_ res
