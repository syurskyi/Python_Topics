c_ Event:
    """A generic class that provides signal/slot functionality"""

    ___  -
        listeners = []

    ___ connect listener):
        listeners.ap..(listener)

    ___ fire *args, **kwargs):
        ___ listener __ listeners:
            listener(*args, **kwargs)
