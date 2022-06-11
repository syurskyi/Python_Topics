# ____ c.. _______ C.., n..
# _______ c__
# _______ __
#
# _______ r__
#
# MARVEL_CSV 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501
#
# Character n..('Character', 'pid name sid align sex first_appearance appearances year')
#
#
# # csv parsing code provided so this Bite can focus on the parsing
#
# ___ _get_csv_data
#     """Download the marvel csv data and return its decoded content"""
#     w__ r__.S.. __ session
#         r.. ?.g.. ? .c__.d.. utf-8
#
#
# ___ load_data
#     """Converts marvel.csv into a sequence of Character namedtuples
#        as defined above"""
#     content ?
#     reader c__.D.. ?.s..  d.._','
#     ___ row __ ?
#         name __.s.. _ (.*?)\(.* r'\1', ? ? .s..
#         y.. ? pid_? page_id' ,
#                         n.._?
#                         sid_ ? ?
#                         align_? ?
#                         sex_? ?
#                         first_appearance_? ?
#                         appearances_? ?
#                         year_? ?
#
#
# characters l.. ?
#
#
# # start coding
#
# ___ most_popular_characters characters_? top=5
#     """Get the most popular character by number of appearances,
#        return top n characters (default 5)
#     """
#     top_lst s.. ?
#                      k.._l.... x i.. ?.a.. __ ?.a.. ____ 0
#                      r.._T.. |t..
#     r.. char.n.. ___ ? __ ?
#
#
# ___ _year_app mon_yr
#     """ return the year based on the MON-YY string from FIRST APPEARANCE field"""
#     year i.. ?.s.. '-' -1
#     r.. s.. 1900 + ? __ ? > 20 ____ s.. 2000 + ?
#
#
# ___ max_and_min_years_new_characters characters_?
#     """Get the year with most and least new characters introduced respectively,
#        use either the 'FIRST APPEARANCE' or 'Year' column in the csv
#        characters, or the 'year' attribute of the namedtuple, return a tuple
#        of (max_year, min_year)
#     """
#     first_app C.. _? c.f.. ___ ? __ ?
#                          __ ?.f..
#     mc ?.m..
#     r.. ? 0 0  ? -1 0
#
#
# ___ get_percentage_female_characters characters_?
#     """Get the percentage of female characters as percentage of all genders
#        over all appearances.
#        Ignore characters that don't have gender ('sex' attribue) set
#        (in your characters data set you should only have Male, Female,
#        Agender and Genderfluid Characters.
#        Return the result rounded to 2 digits
#     """
#     genders C.. c.s__.s.. ' ' 0 ___ ? __ ? __ ?.s..
#     sum_all_genders s.. x 1 ___ ? __ ?.i..
#     r.. r.. 100 * ? Female  / ? 2
