"""This is where we find the Calculator Functionality."""


class Calculator(object):
    """Calculator Class."""

    def add(self, x, y):
        """Addition Function."""
        number_types = (int, long, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
