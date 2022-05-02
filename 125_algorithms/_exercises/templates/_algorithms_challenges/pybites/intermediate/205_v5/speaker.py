# ____ c.. _______ C..
# ____ u__.r.. _______ u..
# ____ p.. _______ P..
#
# _______ g__.d.. __ g..
# ____ ___ _______ B.. __ S..
#
# TMP P..('/tmp')
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
#     speaker_tags ?.f.. c.._'speaker'
#     speaker_list speaker.s...s.. ' ' ___ ? __ ? ___ ? __
#                     ?.s__.r.. '/', ',' .s.. ','
#     r.. first ___ ? *_ __ ?
#
#
# ___ get_percentage_of_female_speakers first_names
#     """Run gender_guesser on the names returning a percentage
#        of female speakers (female and mostly_female),
#        rounded to 2 decimal places."""
#     det g__.D..
#     gender_counts C.. ?.g.. name ___ ? __ ?
#
#     female_count ? 'female'  + ? 'mostly_female'
#     everyone_count s.. n ___ _ ? __ g__.i..
#
#     r.. r.. f.. / ? * 100.0, 2)
#
#
# __ _____ __ _____
#     names ?
#     perc ? ?
#     print ?
