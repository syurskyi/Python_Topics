____ fathers_day _______ get_father_days, generate_father_day_planning

CALENDAR_OUTPUT = """February 23
- Russia

March 19
- Andora
- Bolivia
- Honduras
- Italy
- Liechtenstein
- Portugal
- Spain

May 10
- Romania

May 21
- Germany

June 7
- Austria
- Belgium

June 14
- U.S.
- Canada
- U.K.

June 17
- El Salvador
- Guatemala

June 21
- Egypt
- Jordan
- Lebanon
- Syria
- Uganda

June 23
- Nicaragua
- Poland

August 9
- Samoa
- Brazil

September 6
- Fiji
- New Guinea
- Australia
- New Zealand

November 8
- Estonia
- Finland
- Iceland
- Norway
- Sweden"""


___ test_get_father_days_default
    father_days = get_father_days()
    ... l..(father_days) __ 12
    number_countries = s..(l..(val) ___ val __ father_days.values())
    ... number_countries __ 35
    ... father_days 'June 14'  __  'U.S.', 'Canada', 'U.K.'
    ... father_days 'March 19'  __ [
        'Andora', 'Bolivia', 'Honduras', 'Italy',
        'Liechtenstein', 'Portugal', 'Spain'
    ... father_days 'June 23'  __  'Nicaragua', 'Poland'
    ... father_days 'August 9'  __  'Samoa', 'Brazil'
    ... father_days 'June 7'  __  'Austria', 'Belgium'
    ... father_days 'May 21'  __  'Germany'


___ test_get_father_days_other_years
    father_days = get_father_days y.._2021)
    # changing dates
    ... father_days 'June 20'  __  'U.S.', 'Canada', 'U.K.'
    ... father_days 'August 8'  __  'Samoa', 'Brazil'
    ... father_days 'May 13'  __  'Germany'
    ... father_days 'June 13'  __  'Austria', 'Belgium'
    father_days = get_father_days y.._2022)
    ... father_days 'May 26'  __  'Germany'
    ... father_days 'June 12'  __  'Austria', 'Belgium'
    # remains the same
    ... father_days 'March 19'  __ [
        'Andora', 'Bolivia', 'Honduras', 'Italy',
        'Liechtenstein', 'Portugal', 'Spain'


___ test_generate_father_day_planning(capfd
    generate_father_day_planning()
    actual = ?.r .. 0]
    ... actual.s.. __ CALENDAR_OUTPUT
