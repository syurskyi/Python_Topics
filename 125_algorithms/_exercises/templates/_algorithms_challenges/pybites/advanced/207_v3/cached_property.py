____ functools _______ wraps
____ r__ _______ r__
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


c_ Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    ___ - , color):
        color = color
        _mass = N..

    ___ __repr__
        r.. f'{__class__.__name__}({repr(color)})'

    @cached_property
    ___ mass
        scale_factor = r__()
        sleep(TEMPORAL_SHIFT)
        _mass =  _*{round(scale_factor * GRAVITY_CONSTANT, 4)} '
                      f'{SOLAR_MASS_UNITS}')
        r.. _mass

    mass = property(mass)
