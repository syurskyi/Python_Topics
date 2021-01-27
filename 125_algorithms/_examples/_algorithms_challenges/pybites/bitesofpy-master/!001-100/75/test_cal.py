from cal import get_weekdays

april_1981 = """     April 1981
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""

jan_1986 = """    January 1986
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""

jan_1956 = """    January 1956
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""


def test_april_1981():
    weekdays = get_weekdays(april_1981)
    a__ len(weekdays) == 30
    a__ weekdays[25] == 'Sa'
    a__ weekdays[22] == 'We'


def test_jan_1986():
    weekdays = get_weekdays(jan_1986)
    a__ len(weekdays) == 31
    a__ weekdays[20] == 'Mo'
    a__ weekdays[16] == 'Th'


def test_jan_1956():
    weekdays = get_weekdays(jan_1956)
    a__ len(weekdays) == 31
    a__ weekdays[13] == 'Fr'
    a__ weekdays[31] == 'Tu'