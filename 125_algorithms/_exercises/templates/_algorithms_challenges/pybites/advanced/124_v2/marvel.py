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
#         r.. ?.g.. ? .c__.d.. utf-8
#
#
# ___ load_data
#     """Converts marvel.csv into a sequence of Character namedtuples
#        as defined above"""
#     content _?
#     reader c__.D.. ?.s..  d.._','
#     ___ row __ ?
#         name __.s.. _ .*?)\(.* , r'\1', ? ? .s..
#         y.. ? pid_? page_id
#                         n.._?
#                         sid_? ID
#                         align_ ? ?
#                         sex_ ? ?
#                         appearances_? ?
#                         year_ ? ?
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
#     result C..
#     ___ char __ ?
#         ? ?.n.. + ',' + ?.y.. +_ i.. ?.a.. __ ?.a.. !_ '' ____ 0
#     r.. x 0 .s.. ',' 0 ___ ? __ ?.m.. t..
#
#
# ___ max_and_min_years_new_characters characters_?
#     """Get the year with most and least new characters introduced respectively,
#        use either the 'FIRST APPEARANCE' or 'Year' column in the csv
#        characters, or the 'year' attribute of the namedtuple, return a tuple
#        of (max_year, min_year)
#     """
#     result C..
#     ___ char __ ?
#         __ ?.y.. __ ''
#             _____
#         r.. ?.y.. +_ 1
#     r.. ?.m.. 1 0 0 ?.m.. -1 0
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
#     sexes C..
#     ___ char __ ?
#         __ ?.s.. __ ''
#             _____
#         ? ?.s.. +_ 1
#     r.. r.. f__ ? Female Characters  / f__ s.. ?.v.. * 100.0, 2
