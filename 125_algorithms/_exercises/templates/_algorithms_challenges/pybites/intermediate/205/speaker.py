# ____ c.. _______ i..
# ____ u__.r.. _______ u..
# _______ __
# ____ p.. _______ P..
#
# _______ g__.d.. __ g..
# ____ ___ _______ B.. __ S..
#
# TMP P.. __.g.. "TMP", "/tmp"
# PYCON_HTML ? / "pycon2019.html"
# PYCON_PAGE ('https://bites-data.s3.us-east-2.amazonaws.com/'
#               'pycon2019.html')
#
# __ n.. P__.e..
#     u.. ? ?
#
#
# ___ _get_soup html_?
#     r.. S.. ?.r.. e.._ utf-8 "html.parser"
#
#
# ___ get_pycon_speaker_first_names soup_ N..
#     """Parse the PYCON_HTML using BeautifulSoup, extracting all
#        speakers (class "speaker"). Note that some items contain
#        multiple speakers so you need to extract them.
#        Return a list of first names
#     """
#     __ ? __ N..
#         soup ?
#
#     first_names    # list
#     soup_speakers ?.f.. "span", c.._"speaker"
#     ___ speaker __ ?
#         speaker_clean ?.g.. .s..
#         __ ?.f.. "," > 0
#             ___ s.. __ ?.s.. ","
#                 first_name ?.s...s.. " " 0.s..
#                 ?.a.. ?
#         ____ s__.f.. "/" > 0
#             ___ ? __ ?.s.. "/"
#                 first_name ?.s...s.. " " 0.s..
#                 ?.a.. ?
#         ____
#             f__.a.. s__.s.. " " 0
#     r.. ?
#
#
# ___ get_percentage_of_female_speakers first_names
#     """Run gender_guesser on the names returning a percentage
#        of female speakers (female and mostly_female),
#        rounded to 2 decimal places."""
#     female_counter 0
#     gender_guess g__.D..
#     ___ name __ fi..
#         predicted_gender g__.g.. ?
#         __ ? __ "female", "mostly_female"
#             f.. +_ 1
#
#     r.. r.. f../l.. f..)*100), 2
#
# __ _____ __ _____
#     names ?
#     perc ? ?
#     print ?