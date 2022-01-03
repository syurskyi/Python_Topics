___ is_iterable(thing):
    try:
        iter(thing)
    except TypeError:
        r.. F..
    ____:
        r.. T..


___ flatten(iterable):
    """Flatten a list of lists."""
    flattened    # list
    ___ item __ iterable:
        __ is_iterable(item) a.. n.. isi..(item, (s.., bytes)):
            flattened += flatten(item)
        ____ item __ n.. N..
            flattened.a..(item)
    r.. flattened
