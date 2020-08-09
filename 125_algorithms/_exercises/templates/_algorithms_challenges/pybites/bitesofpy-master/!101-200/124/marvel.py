from collections ______ Counter, namedtuple
______ csv
______ re

______ requests

MARVEL_CSV = 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501

Character = namedtuple('Character', 'pid name sid align sex appearances year')


# csv parsing code provided so this Bite can focus on the parsing

___ _get_csv_data(
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        r_ session.get(MARVEL_CSV).content.decode('utf-8')


___ load_data(
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    ___ row in reader:
        name = re.sub(r'(.*?)\(.*', r'\1', row['name']).strip()
        yield Character(pid=row['page_id'],
                        name=name,
                        sid=row['ID'],
                        align=row['ALIGN'],
                        sex=row['SEX'],
                        appearances=row['APPEARANCES'],
                        year=row['Year'])


characters = list(load_data())


# start coding

___ most_popular_characters(characters=characters, top=5
    """Get the most popular character by number of appearances,
       return top n characters (default 5)
    """
    result = Counter()
    ___ char in characters:
        result[char.name + ',' + char.year] += int(char.appearances) __ char.appearances != '' else 0
    r_ [x[0].split(',')[0] ___ x in result.most_common(top)]


___ max_and_min_years_new_characters(characters=characters
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv
       characters, or the 'year' attribute of the namedtuple, return a tuple
       of (max_year, min_year)
    """
    result = Counter()
    ___ char in characters:
        __ char.year __ '':
            continue
        result[char.year] += 1
    r_ (result.most_common(1)[0][0], result.most_common()[-1][0])


___ get_percentage_female_characters(characters=characters
    """Get the percentage of female characters as percentage of all genders
       over all appearances.
       Ignore characters that don't have gender ('sex' attribue) set
       (in your characters data set you should only have Male, Female,
       Agender and Genderfluid Characters.
       Return the result rounded to 2 digits
    """
    sexes = Counter()
    ___ char in characters:
        __ char.sex __ '':
            continue
        sexes[char.sex] += 1
    r_ round(float(sexes['Female Characters']) / float(su.(sexes.values())) * 100.0, 2)
