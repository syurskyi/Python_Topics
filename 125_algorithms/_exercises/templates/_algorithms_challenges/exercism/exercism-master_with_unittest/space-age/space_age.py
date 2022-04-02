c_ SpaceAge:

    ORBITAL_PERIODS = {
        'mercury': 7600530.24,
        'venus': 19413907.2,
        'earth': 31558149.76,
        'mars': 59354294.4,
        'jupiter': 374335776.0,
        'saturn': 929596608.0,
        'uranus': 2661041808.0,
        'neptune': 5200418592.0
    }

    ___ - , seconds
        seconds = seconds

    ___ on_planet  planet
        r.. r..(seconds / ORBITAL_PERIODS[planet], 2)


___ add_on_planet_fn(planet
    setattr(SpaceAge, 'on_' + planet, l.... self: on_planet(planet))


___ planet __ l..(SpaceAge.ORBITAL_PERIODS.k..
    add_on_planet_fn(planet)
