c_ Event:
    """A generic class that provides signal/slot functionality"""

    ___  -
        listeners = []

    ___ connect listener):
        listeners.append(listener)

    ___ fire *args, **kwargs):
        for listener in listeners:
            listener(*args, **kwargs)
