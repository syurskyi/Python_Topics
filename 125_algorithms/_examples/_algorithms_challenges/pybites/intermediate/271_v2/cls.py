import inspect


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""

    

    return [name for name,_ in inspect.getmembers(mod,inspect.isclass) if name[0].isupper()]

