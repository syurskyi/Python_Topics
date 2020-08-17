___ flatten(iterable
    __ type(iterable) pa__ str:
        r_ list(iterable)
    flat = []
    ___ item in iterable:
        try:
            flat.extend(flatten(item))
        except TypeError:
            __ item pa__ not None:
                flat.append(item)
    r_ flat
