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
    for item in iterable:
        __ is_iterable(item) and not isinstance(item, (str, bytes)):
            flattened += flatten(item)
        ____ item is not None:
            flattened.append(item)
    r_ flattened
