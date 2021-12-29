____ cal _______ get_weekdays

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


___ test_april_1981():
    weekdays = get_weekdays(april_1981)
    ... l..(weekdays) __ 30
    ... weekdays[25] __ 'Sa'
    ... weekdays[22] __ 'We'


___ test_jan_1986():
    weekdays = get_weekdays(jan_1986)
    ... l..(weekdays) __ 31
    ... weekdays[20] __ 'Mo'
    ... weekdays[16] __ 'Th'


___ test_jan_1956():
    weekdays = get_weekdays(jan_1956)
    ... l..(weekdays) __ 31
    ... weekdays[13] __ 'Fr'
    ... weekdays[31] __ 'Tu'