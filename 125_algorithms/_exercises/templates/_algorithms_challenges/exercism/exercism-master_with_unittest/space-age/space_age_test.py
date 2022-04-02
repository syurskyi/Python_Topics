_______ unittest

____ space_age _______ SpaceAge


c_ SpaceAgeTest(unittest.TestCase
    ___ test_age_in_seconds
        age = SpaceAge(1e6)
        assertEqual(1e6, age.seconds)

    ___ test_age_in_earth_years
        age = SpaceAge(1e9)
        assertEqual(31.69, age.on_earth())

    ___ test_age_in_mercury_years
        age = SpaceAge(2134835688)
        assertEqual(67.65, age.on_earth())
        assertEqual(280.88, age.on_mercury())

    ___ test_age_in_venus_years
        age = SpaceAge(189839836)
        assertEqual(6.02, age.on_earth())
        assertEqual(9.78, age.on_venus())

    ___ test_age_on_mars
        age = SpaceAge(2329871239)
        assertEqual(73.83, age.on_earth())
        assertEqual(39.25, age.on_mars())

    ___ test_age_on_jupiter
        age = SpaceAge(901876382)
        assertEqual(28.58, age.on_earth())
        assertEqual(2.41, age.on_jupiter())

    ___ test_age_on_saturn
        age = SpaceAge(3e9)
        assertEqual(95.06, age.on_earth())
        assertEqual(3.23, age.on_saturn())

    ___ test_age_on_uranus
        age = SpaceAge(3210123456)
        assertEqual(101.72, age.on_earth())
        assertEqual(1.21, age.on_uranus())

    ___ test_age_on_neptune
        age = SpaceAge(8210123456)
        assertEqual(260.16, age.on_earth())
        assertEqual(1.58, age.on_neptune())


__ _____ __ _____
    unittest.main()
