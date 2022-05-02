# _______ g__.d.. __ g..
# ____ ___ _______ B.. __ S..
# _______ r__
# _______ __
#
# PYCON_HTML 'https://bites-data.s3.us-east-2.amazonaws.com/pycon2019.html'
#
# ___ _get_soup html_?
#     response r__.g.. P..
#     r.. S.. ?.c.. "html.parser"
#
#
# ___ get_pycon_speaker_first_names soup_ N..
#     """Parse the PYCON_HTML using BeautifulSoup, extracting all
#        speakers (class "speaker"). Note that some items contain
#        multiple speakers so you need to extract them.
#        Return a list of first names
#     """
#     soup ?
#
#     speakers    # list
#     ___ speaker __ ?.f.. 'span', 'speaker'
#         s.. ?.t__.s..
#
#         # Multiple speakers separated by comma
#         __ __.m.. _ .*,.* s..
#             multiple_speakers ?.s.. ', '
#             ___ s __ ?
#                 s__.a..?.s..  0
#
#         # Multiple speakers seperated by slash
#         ____ __.m.. _ .*/.*  s..
#             m.. ?.s.. ' / '
#             ___ s __ ?
#                 s__.a.. ?.s..  0
#
#         # Speaker name begins with acronym
#         ____ __.m.. _ [A-Z]\. ?
#             s_.a.. ?.s.. 1
#
#         ____
#             ?.a.. ?.s..  0
#
#     r.. ?
#
#
# ___ get_percentage_of_female_speakers first_names
#     """Run gender_guesser on the names returning a percentage
#        of female speakers (female and mostly_female),
#        rounded to 2 decimal places."""
#     d g__.D.. c.._F..
#     genders ?.g.. ? ___ ? __ f..
#     total_speakers l.. ?
#     female_speakers l.. g ___ ? __ g.. __ ? __ 'female' o. ? __ 'mostly_female'
#     r.. r.. ? / t.. * 100, 2
#
#
# __ _____ __ _____
#     names ?
#     perc ? ?
#     print ?