_______ __
____ p.. _______ P..
____ u__.r.. _______ u..
_______ __
_______ d__

____ c.. _______ d..
____ dateutil.parser _______ p..

# get the data
TMP = P..(__.g..("TMP", "/tmp"
base_url = 'https://bites-data.s3.us-east-2.amazonaws.com/'

fathers_days_countries = TMP / 'fathers-day-countries.txt'
fathers_days_recurring = TMP / 'fathers-day-recurring.txt'

___ file_ __ (fathers_days_countries, fathers_days_recurring
    __ n.. file_.exists
        u..(base_url + file_.name, file_)


___ _parse_father_days_per_country(year, date_to_countries,filename=fathers_days_countries
    """Helper to parse fathers_days_countries"""
    year = s..(year)
    w__ o.. filename _ __ f:

        ___ line __ f:
            line = line.s..
            __ n.. line o. line.startswith('#'
                _____
            ____ line.startswith('*'

                line = __.sub(r'\band\b','',line)

                countries =  l.. m..(l.... s: s.s..('* ').s..,line.s..(',')))
            ____
                date,day = line.s..(':')

                __ date __ year:
                    day = day.s..
                    date_to_countries[day].e.. countries)


___ _parse_recurring_father_days(days_to_countries,filename=fathers_days_recurring
    """Helper to parse fathers_days_recurring"""


    w__ o.. filename _ __ f:
        ___ line __ f:
            line = line.s..
            __ n.. line o. line.startswith('#'
                _____
            __ line.startswith('*'
                date = line[2:]
            ____
                days_to_countries[date].a..(line)



    






___ get_father_days y.._2020
    """Returns a dictionary of keys = dates and values = lists
       of countries that celebrate Father's day that date

       Consider using the the 2 _parse* helpers.
    """
    days_to_countries = d..(l..)

    _parse_father_days_per_country(year,days_to_countries)
    _parse_recurring_father_days(days_to_countries)

    r.. days_to_countries
















___ generate_father_day_planning(days_to_countries_ N..
    """Prints all father days in order, example in tests and
       Bite description
    """
    __ days_to_countries __ N..
        days_to_countries = get_father_days()

    dates = l..(days_to_countries.keys


    ___ i,date __ e..(dates
        dates[i] = p..(date,default=d__.d__(2020,1,1
        #days_to_countries[date].sort()



    dates.s..()


    ___ date __ dates:
        date = date.s..('%B %d')
        date = __.sub(r'0(\d)',r'\1',date)

        countries = days_to_countries[date]

        print(date)

        ___ country __ countries:
            print _*- {country}')

        print()


    # you code



__ _______ __ _______

    generate_father_day_planning()
