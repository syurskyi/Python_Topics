# ____ c.. _______ C.., n..
# _______ c__
# _______ __
#
# _______ r__
#
# MARVEL_CSV 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501
#
# Character n..('Character', 'pid name sid align sex appearances year')
#
#
# # csv parsing code provided so this Bite can focus on the parsing
#
# ___ _get_csv_data
#     """Download the marvel csv data and return its decoded content"""
#     w__ r__.S.. __ session
#         r.. ?.g.. M.. .c__.d.. utf-8
#
#
# ___ load_data
#     """Converts marvel.csv into a sequence of Character namedtuples
#        as defined above"""
#     content ?
#     reader c__.D.. ?.s..  d.._','
#     ___ row __ ?
#         name __.s.. _ (.*?)\(.*', r'\1', row 'name' ).s..
#         y.. C.. (pid_? page_id
#                         n.._?
#                         sid_? ID
#                         align_? ALIGN
#                         sex_? SEX
#                         appearances_? APPEARANCES
#                         year_? Year
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
#
#
#     character_counts C..
#
#     ___ character __ ?
#         __ ?.a..
#             __ ?.n.. n.. __ c.. o. (?.n.. __ c.. a.. i.. ?.a.. > c.. ?.n..
#                 c.. ?.n.. i.. ?.a..
#
#     r.. [?[0] ___ ? __ c__.m.. t..
#
#
#
#
# ___ max_and_min_years_new_characters characters_?
#     """Get the year with most and least new characters introduced respectively,
#        use either the 'FIRST APPEARANCE' or 'Year' column in the csv
#        characters, or the 'year' attribute of the namedtuple, return a tuple
#        of (max_year, min_year)
#     """
#
#     most_year min_year=N..
#     year_counts C..
#
#     ___ character __ ?
#         __ ?.y..
#             y.. ?.y.. +_ 1
#
#
#
#     years y__.m..
#     most_year ? 0 0
#     least_year ? -1 0
#
#
#     r.. ? ?
#
#
#
#
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
#
#
#
#     sex_counts C..
#
#
#     ___ character __ ?
#         __ ?.s..
#             s.. ?.s.. +_ 1
#
#
#
#
#
#     total s.. s__.v..
#     females s.. 'Female Characters'
#     print s..
#
#     r.. r.. ?/?* 100,2
#
#
#
#
#
#
#
