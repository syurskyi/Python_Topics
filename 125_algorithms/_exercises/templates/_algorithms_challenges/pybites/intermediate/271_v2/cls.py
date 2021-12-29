import inspect


___ get_classes(mod):
    """Return a list of all classes in module 'mod'"""

    

    return [name for name,_ in inspect.getmembers(mod,inspect.isclass) __ name[0].isupper()]

