____ functools _______ wraps
____ random _______ random
____ time _______ sleep


___ cached_property(func):
    """decorator used to cache expensive object attribute lookup"""

    @wraps(func)
    ___ getter(self, *args, **kwargs):
        __ n.. hasattr(cached_property, "cache"):
            cached_property.cache = d..()
        __ func n.. __ cached_property.cache:
            cached_property.cache[func] = func(self)
        r.. cached_property.cache[func]

    r.. getter


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    ___ __init__(self, color):
        self.color = color
        self._mass = N..

    ___ __repr__(self):
        r.. f'{self.__class__.__name__}({repr(self.color)})'

    @cached_property
    ___ mass(self):
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                      f'{self.SOLAR_MASS_UNITS}')
        r.. self._mass

    mass = property(mass)
