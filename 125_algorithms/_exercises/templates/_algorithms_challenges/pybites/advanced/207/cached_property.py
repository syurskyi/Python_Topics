____ r__ _______ r__
____ time _______ sleep
____ functools _______ wraps


___ cached_property(func
    """decorator used to cache expensive object attribute lookup"""
    cache = N..
    @wraps(func)
    ___ wrapper $ $$:
        nonlocal cache
        __ cache __ N..
            cache = func $ $$
        r.. cache
    r.. wrapper


c_ Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'

    ___ - , color
        color = color
        _mass = N..

    ___  -r
        r.. f'{__class__.__name__}({r.. (color)})'

    @cached_property
    ___ mass
        scale_factor = r__()
        sleep(TEMPORAL_SHIFT)
        _mass =  _*{r..(scale_factor * GRAVITY_CONSTANT, 4)} '
                      f'{SOLAR_MASS_UNITS}')
        r.. _mass

    ___ __setattr__  var, val
        __ var __ 'mass':
            r.. AttributeError
        ____:
            super(Planet, self).__setattr__(var, val)
    # @mass.setter
    # def mass(self, value):
    #     self._mass = value
