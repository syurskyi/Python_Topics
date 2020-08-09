___ flatten(iterable
    __ type(iterable) is str:
        r_ list(iterable)
    flat = []
    for item in iterable:
        try:
            flat.extend(flatten(item))
        except TypeError:
            __ item is not None:
                flat.append(item)
    r_ flat
