# Named Tuples - DocStrings and Default Values

from collections import namedtuple

# Adding DocStrings to Named Tuples
# This is easy to do, both with the generated class, as well as it's properties.

Point2D = namedtuple('Point2D', 'x y')
Point2D.__doc__ = 'Represents a 2D Cartesian coordinate'

# And we can even add docstrings to the properties:

Point2D.x.__doc__ = 'x-coordinate'
Point2D.y.__doc__ = 'y-coordinate'
help(Point2D)
