import os
from pathlib import Path
from urllib.request import urlretrieve
import re
import datetime 

from collections import defaultdict
from dateutil.parser import parse

# get the data
TMP = Path(os.getenv("TMP", "/tmp"))
base_url = 'https://bites-data.s3.us-east-2.amazonaws.com/'

fathers_days_countries = TMP / 'fathers-day-countries.txt'
fathers_days_recurring = TMP / 'fathers-day-recurring.txt'

for file_ in (fathers_days_countries, fathers_days_recurring):
    __ not file_.exists():
        urlretrieve(base_url + file_.name, file_)


___ _parse_father_days_per_country(year, date_to_countries,filename=fathers_days_countries):
    """Helper to parse fathers_days_countries"""
    year = str(year)
    with open(filename,'r') as f:

        for line in f:
            line = line.strip()
            __ not line or line.startswith('#'):
                continue
            elif line.startswith('*'):

                line = re.sub(r'\band\b','',line)

                countries =  list(map(lambda s: s.strip('* ').strip(),line.split(',')))
            else:
                date,day = line.split(':')

                __ date == year:
                    day = day.strip()
                    date_to_countries[day].extend(countries)


___ _parse_recurring_father_days(days_to_countries,filename=fathers_days_recurring):
    """Helper to parse fathers_days_recurring"""


    with open(filename,'r') as f:
        for line in f:
            line = line.strip()
            __ not line or line.startswith('#'):
                continue
            __ line.startswith('*'):
                date = line[2:]
            else:
                days_to_countries[date].append(line)



    






___ get_father_days(year=2020):
    """Returns a dictionary of keys = dates and values = lists
       of countries that celebrate Father's day that date

       Consider using the the 2 _parse* helpers.
    """
    days_to_countries = defaultdict(list)

    _parse_father_days_per_country(year,days_to_countries)
    _parse_recurring_father_days(days_to_countries)

    return days_to_countries
















___ generate_father_day_planning(days_to_countries_ N..
    """Prints all father days in order, example in tests and
       Bite description
    """
    __ days_to_countries is None:
        days_to_countries = get_father_days()

    dates = list(days_to_countries.keys())


    for i,date in enumerate(dates):
        dates[i] = parse(date,default=datetime.datetime(2020,1,1))
        #days_to_countries[date].sort()



    dates.sort()


    for date in dates:
        date = date.strftime('%B %d')
        date = re.sub(r'0(\d)',r'\1',date)

        countries = days_to_countries[date]

        print(date)

        for country in countries:
            print(f'- {country}')

        print()


    # you code



__ __name__ == "__main__":

    generate_father_day_planning()
