____ r__ _______ r__
____ t__ _______ sleep
____ f.. _______ w..


___ cached_property(func
    """decorator used to cache expensive object attribute lookup"""
    cache N..
    $w.. f..
    ___ wrapper $ $$
        nonlocal cache
        __ cache __ N..
            cache func $ $$
        r.. cache
    r.. ?


c_ Planet:
    """the nicest little orb this side of Orion's Belt"""

    GRAVITY_CONSTANT 42
    TEMPORAL_SHIFT 0.12345
    SOLAR_MASS_UNITS 'M\N{SUN}'

    ___ - , color
        ? ?
        _mass N..

    ___  -r
        r.. _*  -c.-n ({r.. (color)})'

    @cached_property
    ___ mass
        scale_factor r__()
        sleep(TEMPORAL_SHIFT)
        _mass =  _*{r..(scale_factor * GRAVITY_CONSTANT, 4)} '
                      _* SOLAR_MASS_UNITS}')
        r.. _mass

    ___ __setattr__  var, val
        __ var __ 'mass':
            r.. AttributeError
        ____
            super(Planet, self).__setattr__(var, val)
    # @mass.setter
    # def mass(self, value):
    #     self._mass = value
