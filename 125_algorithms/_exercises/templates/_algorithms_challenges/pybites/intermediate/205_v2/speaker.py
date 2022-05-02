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
#
#     speakers ?.f.. 'span',c.._'speaker'
#
#     first_names    # list
#
#     ___ speaker __ ?
#         text ?.g.. s..=T..
#         result __.s.. _ \s*,|/\s* ?
#         f__.e.. r.s.. 0 ___ ? __ ?
#
#     r.. ?
#
#
# ___ get_percentage_of_female_speakers first_names
#     """Run gender_guesser on the names returning a percentage
#        of female speakers (female and mostly_female),
#        rounded to 2 decimal places."""
#
#     d g__.D.. c.._F..
#     labels ('mostly_female','female')
#     female_count 0
#     ___ first_name __ f..
#         result d.g.. ?
#
#         f.. +_ ? __ l..
#
#     r.. r.. f../l.. ? 2
#
#
# __ _____ __ _____
#     names ?
#     perc ? ?
#     print ?
