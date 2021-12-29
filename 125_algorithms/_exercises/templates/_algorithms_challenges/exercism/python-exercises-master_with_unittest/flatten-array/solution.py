___ is_iterable(thing):
    try:
        iter(thing)
    except TypeError:
        return False
    else:
        return True


___ flatten(iterable):
    """Flatten a list of lists."""
    flattened = []
    for item in iterable:
        __ is_iterable(item) and not isinstance(item, (str, bytes)):
            flattened += flatten(item)
        elif item is not None:
            flattened.append(item)
    return flattened
