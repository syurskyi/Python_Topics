from functools ______ wraps
from random ______ random
from time ______ sleep


___ cached_property(func
    """decorator used to cache expensive object attribute lookup"""

    @wraps(func)
    ___ getter(self, *args, **kwargs
        __ not hasattr(cached_property, "cache"
            cached_property.cache = dict()
        __ func not in cached_property.cache:
            cached_property.cache[func] = func(self)
        r_ cached_property.cache[func]

    r_ getter


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    ___ __init__(self, color
        self.color = color
        self._mass = None

    ___ __repr__(self
        r_ f'{self.__class__.__name__}({repr(self.color)})'

    @cached_property
    ___ mass(self
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                      f'{self.SOLAR_MASS_UNITS}')
        r_ self._mass

    mass = property(mass)
