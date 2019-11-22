# Lazy Iterables

# Lazy evaluation is when evaluating a value is deferred until it is actually requested.
# Simple examples of lazy evaluation are often seen in classes for calculated properties.
# As you can see, in this circle class, every time we set the radius, we re-calculate and store the area.
# When we request the area of the circle, we simply return the stored value.

import math

class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.area = math.pi * r ** 2


c = Circle(1)
c.area
c.radius = 2
c.radius, c.area

# Simple examples of lazy evaluation are often seen in classes for calculated properties.
#
# But instead of doing it this way, we could just calculate the area every time
# it is requested without actually storing the value

class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r

    @property
    def area(self):
        return math.pi * self.radius ** 2


c = Circle(1)
c.area
c.radius = 2
c.area


# Simple examples of lazy evaluation are often seen in classes for calculated properties.

class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            print('Calculating area...')
            self._area = math.pi * self.radius ** 2
        return self._area


c = Circle(1)
c.area
c.area
c.radius = 2
c.area
