____ d__ _______ d__
_______ json
_______ __
____ p.. _______ P..
____ u__.r.. _______ u..

_______ p__

____ zodiac _______ (get_signs, get_sign_with_most_famous_people,
                    signs_are_mutually_compatible, get_sign_by_date, Sign)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = __.g.. TMP  /tmp
PATH = P..(TMP, "zodiac.json")


?p__.f..(scope='module')
___ signs
    __ n.. PATH.exists
        u..(URL, PATH)
    w__ o.. PATH) __ f:
        data = json.loads(f.read
    r.. get_signs(data)


# write your pytest code here ...
___ test_named_tuple(signs
    ... l..(Sign._fields) __ l..('name compatibility famous_people sun_dates'.s..(' '
    ... r.. (signs[0]).s.. 'Sign(')


___ test_get_signs(signs
    ... l..(signs) __ 12


___ test_get_sign_with_most_famouse_people(signs
    ... get_sign_with_most_famous_people(signs) __ ('Scorpio', 35)


?p__.m__.p.("sgn1, sgn2, result", [
    ('Aries', 'Aries', F..),
    ('Aries', 'Leo', T..),
    ('Aries', 'Capricorn', F..),
    ('Aries', 'Aquarius', T..)
])
___ test_signs_are_mutually_compatible(signs, sgn1, sgn2, result
    ... signs_are_mutually_compatible(signs, sgn1, sgn2) __ result


?p__.m__.p.("dt, result", [
    ([3, 21], 'Aries'),
    ([4, 19], 'Aries'),
    ([4, 20], 'Taurus'),
    ([5, 20], 'Taurus'),
    ([5, 21], 'Gemini'),
    ([6, 20], 'Gemini'),
    ([6, 21], 'Cancer'),
    ([7, 22], 'Cancer'),
    ([7, 23], 'Leo'),
    ([8, 22], 'Leo'),
    ([8, 23], 'Virgo'),
    ([9, 22], 'Virgo'),
    ([9, 23], 'Libra'),
    ([10, 22], 'Libra'),
    ([10, 23], 'Scorpio'),
    ([11, 21], 'Scorpio'),
    ([11, 22], 'Sagittarius'),
    ([12, 21], 'Sagittarius'),
    ([12, 22], 'Capricorn'),  # should be 'Capricorn' but there's a bug in the code!!
    ([1, 19], 'Capricorn'),  # should be 'Capricorn' but there's a bug in the code!!
    ([1, 20], 'Aquarius'),
    ([2, 18], 'Aquarius'),
    ([2, 19], 'Pisces'),
    ([3, 20], 'Pisces')
])
___ test_get_sign_by_date(signs, dt, result
    m, d = dt
    ... get_sign_by_date(signs, d__ y.._2000,  m.._m,  d.._d __ result
