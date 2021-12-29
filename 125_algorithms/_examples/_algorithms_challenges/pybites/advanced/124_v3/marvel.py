from collections import Counter, namedtuple
import csv
import re

import requests

MARVEL_CSV = 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501

Character = namedtuple('Character', 'pid name sid align sex first_appearance appearances year')


# csv parsing code provided so this Bite can focus on the parsing

def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode('utf-8')


def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        name = re.sub(r'(.*?)\(.*', r'\1', row['name']).strip()
        yield Character(pid=row['page_id'],
                        name=name,
                        sid=row['ID'],
                        align=row['ALIGN'],
                        sex=row['SEX'],
                        first_appearance=row['FIRST APPEARANCE'],
                        appearances=row['APPEARANCES'],
                        year=row['Year'])


characters = list(load_data())


# start coding

def most_popular_characters(characters=characters, top=5):
    """Get the most popular character by number of appearances,
       return top n characters (default 5)
    """
    top_lst = sorted(characters,
                     key=lambda x: int(x.appearances) if x.appearances else 0,
                     reverse=True)[:top]
    return [char.name for char in top_lst]


def _year_app(mon_yr):
    """ return the year based on the MON-YY string from FIRST APPEARANCE field"""
    year = int(mon_yr.split('-')[-1])
    return str(1900 + year) if year > 20 else str(2000 + year)


def max_and_min_years_new_characters(characters=characters):
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv
       characters, or the 'year' attribute of the namedtuple, return a tuple
       of (max_year, min_year)
    """
    first_app = Counter([_year_app(c.first_appearance) for c in characters
                         if c.first_appearance])
    mc = first_app.most_common()
    return mc[0][0], mc[-1][0]


def get_percentage_female_characters(characters=characters):
    """Get the percentage of female characters as percentage of all genders
       over all appearances.
       Ignore characters that don't have gender ('sex' attribue) set
       (in your characters data set you should only have Male, Female,
       Agender and Genderfluid Characters.
       Return the result rounded to 2 digits
    """
    genders = Counter([c.sex.split(' ')[0] for c in characters if c.sex])
    sum_all_genders = sum([x[1] for x in genders.items()])
    return round(100 * genders['Female'] / sum_all_genders, 2)
