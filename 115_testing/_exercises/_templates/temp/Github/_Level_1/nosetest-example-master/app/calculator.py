"""This is where we find the Calculator Functionality."""


c_ Calculator(object):
    """Calculator Class."""

    ___ add  x, y):
        """Addition Function."""
        number_types = (int, long, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError