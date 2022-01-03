_______ unittest

____ space_age _______ SpaceAge


c_ SpaceAgeTest(unittest.TestCase):
    ___ test_age_in_seconds
        age = SpaceAge(1e6)
        assertEqual(age.seconds, 1e6)

    ___ test_age_in_earth_years
        age = SpaceAge(1e9)
        assertEqual(age.on_earth(), 31.69)

    ___ test_age_in_mercury_years
        age = SpaceAge(2134835688)
        assertEqual(age.on_earth(), 67.65)
        assertEqual(age.on_mercury(), 280.88)

    ___ test_age_in_venus_years
        age = SpaceAge(189839836)
        assertEqual(age.on_earth(), 6.02)
        assertEqual(age.on_venus(), 9.78)

    ___ test_age_on_mars
        age = SpaceAge(2329871239)
        assertEqual(age.on_earth(), 73.83)
        assertEqual(age.on_mars(), 39.25)

    ___ test_age_on_jupiter
        age = SpaceAge(901876382)
        assertEqual(age.on_earth(), 28.58)
        assertEqual(age.on_jupiter(), 2.41)

    ___ test_age_on_saturn
        age = SpaceAge(3e9)
        assertEqual(age.on_earth(), 95.06)
        assertEqual(age.on_saturn(), 3.23)

    ___ test_age_on_uranus
        age = SpaceAge(3210123456)
        assertEqual(age.on_earth(), 101.72)
        assertEqual(age.on_uranus(), 1.21)

    ___ test_age_on_neptune
        age = SpaceAge(8210123456)
        assertEqual(age.on_earth(), 260.16)
        assertEqual(age.on_neptune(), 1.58)


__ __name__ __ '__main__':
    unittest.main()
