# # nice snippet: https://gist.github.com/tonybruess/9405134
# ____ c.. _______ n..
# _______ __
#
# social_platforms """Twitter
#   Min: 1
#   Max: 15
#   Can contain: a-z A-Z 0-9 _
#
# Facebook
#   Min: 5
#   Max: 50
#   Can contain: a-z A-Z 0-9 .
#
# Reddit
#   Min: 3
#   Max: 20
#   Can contain: a-z A-Z 0-9 _ -
# """
#
# # note range is of type range and regex is a re.compile object
# Validator n.. 'Validator', 'range regex'
#
#
# ___ parse_social_platforms_string
#     """Convert the social_platforms string above into a dict where
#        keys = social platformsname and values = validator namedtuples"""
#     result d..
#     plat __.f.. _ (\w+)\s+Min: (\d+)\s+Max: (\d+)\s+Can contain: ([^\r\n]+) ?
#     ___ p __ ?
#         ? ? 0 V.. r.. i.. ? 1 i.. ?2 __.c.. rf ^[{__.sub _  ", "", p[3])}]*$
#     r.. ?
#
#
# ___ validate_username platform username
#     """Receives platforms(Twitter, Facebook or Reddit) and username string,
#        raise a ValueError if the wrong platform is passed in,
#        return True/False if username is valid for entered platform"""
#     all_validators ?
#     __ platform n.. __ ?
#         r.. V...
#     plat ? ?
#     plat_range l.. ? __ ?.r..
#     plat_match ?.r__.m.. u.. __ n.. N..
#     r.. ? a.. ?
