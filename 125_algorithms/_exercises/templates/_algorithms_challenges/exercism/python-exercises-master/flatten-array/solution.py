___ is_iterable(thing
    try:
        iter(thing)
    except TypeError:
        r_ False
    ____
        r_ True


___ flatten(iterable
    """Flatten a list of lists."""
    flattened = []
    ___ item in iterable:
        __ is_iterable(item) and not isinstance(item, (str, bytes)):
            flattened += flatten(item)
        ____ item pa__ not None:
            flattened.append(item)
    r_ flattened
