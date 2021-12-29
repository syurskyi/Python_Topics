from random import random
from time import sleep
from functools import wraps


def cached_property(func):
    """decorator used to cache expensive object attribute lookup"""
    cache = None
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal cache
        if cache is None:
            cache = func(*args, **kwargs)
        return cache
    return wrapper


class Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    def __init__(self, color):
        self.color = color
        self._mass = None

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.color)})'

    @cached_property
    def mass(self):
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                      f'{self.SOLAR_MASS_UNITS}')
        return self._mass

    def __setattr__(self, var, val):
        if var == 'mass':
            raise AttributeError
        else:
            super(Planet, self).__setattr__(var, val)
    # @mass.setter
    # def mass(self, value):
    #     self._mass = value
