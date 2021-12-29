____ random _______ random
____ time _______ sleep
____ functools _______ wraps


___ cached_property(func):
    """decorator used to cache expensive object attribute lookup"""
    cache = N..
    @wraps(func)
    ___ wrapper(*args, **kwargs):
        nonlocal cache
        __ cache __ N..
            cache = func(*args, **kwargs)
        r.. cache
    r.. wrapper


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

    ___ __setattr__(self, var, val):
        __ var __ 'mass':
            raise AttributeError
        ____:
            super(Planet, self).__setattr__(var, val)
    # @mass.setter
    # def mass(self, value):
    #     self._mass = value
