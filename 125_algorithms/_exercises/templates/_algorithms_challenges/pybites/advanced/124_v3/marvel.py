____ c.. _______ C.., n..
_______ csv
_______ __

_______ r__

MARVEL_CSV = 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501

Character = n..('Character', 'pid name sid align sex first_appearance appearances year')


# csv parsing code provided so this Bite can focus on the parsing

___ _get_csv_data
    """Download the marvel csv data and return its decoded content"""
    w__ r__.S.. __ session:
        r.. session.g.. MARVEL_CSV).content.d.. 'utf-8')


___ load_data
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.s.. , delimiter=',')
    ___ row __ reader:
        name = __.sub(r'(.*?)\(.*', r'\1', row 'name' ).s..
        y.. Character(pid=row 'page_id' ,
                        name=name,
                        sid=row 'ID' ,
                        align=row 'ALIGN' ,
                        sex=row 'SEX' ,
                        first_appearance=row 'FIRST APPEARANCE' ,
                        appearances=row 'APPEARANCES' ,
                        year=row 'Year' )


characters = l..(load_data


# start coding

___ most_popular_characters(characters=characters, top=5
    """Get the most popular character by number of appearances,
       return top n characters (default 5)
    """
    top_lst = s..(characters,
                     key=l.... x: i..(x.appearances) __ x.appearances ____ 0,
                     r.._T..[:top]
    r.. [char.name ___ char __ top_lst]


___ _year_app(mon_yr
    """ return the year based on the MON-YY string from FIRST APPEARANCE field"""
    year = i..(mon_yr.s..('-')[-1])
    r.. s..(1900 + year) __ year > 20 ____ s..(2000 + year)


___ max_and_min_years_new_characters(characters=characters
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv
       characters, or the 'year' attribute of the namedtuple, return a tuple
       of (max_year, min_year)
    """
    first_app = C..([_year_app(c.first_appearance) ___ c __ characters
                         __ c.first_appearance])
    mc = first_app.m..
    r.. mc[0][0], mc[-1][0]


___ get_percentage_female_characters(characters=characters
    """Get the percentage of female characters as percentage of all genders
       over all appearances.
       Ignore characters that don't have gender ('sex' attribue) set
       (in your characters data set you should only have Male, Female,
       Agender and Genderfluid Characters.
       Return the result rounded to 2 digits
    """
    genders = C..([c.sex.s..(' ')[0] ___ c __ characters __ c.sex])
    sum_all_genders = s..([x[1] ___ x __ genders.i..])
    r.. r..(100 * genders 'Female'  / sum_all_genders, 2)
