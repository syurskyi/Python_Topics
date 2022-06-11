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
#     platforms s__.s.. '\n\n'
#
#     platform_to_validator    # dict
#
#     ___ platform __ platforms:
#         result __.s.. _ (.+)\n.*Min: (\d+)\n.*Max: (\d+)\n.+: (.+) ,platform,flags=__.M
#
#         values    # list
#         ___ i __ r.. 1,5
#             ?.a.. r__.g.. i
#         platform_name ? 0
#         range_object r.. i.. ? 1 i.. ? 2
#         last ''.j.. ? -1 .s..
#         regex '^ ' + ? + ' +$'
#         r __.c.. ?
#         validator ? r.. ?
#         p.. p.3. ?
#
#
#     r.. ?
#
#
# ___ validate_username platform username
#     """Receives platforms(Twitter, Facebook or Reddit) and username string,
#        raise a ValueError if the wrong platform is passed in,
#        return True/False if username is valid for entered platform"""
#     all_validators ?
#
#     __ ? n.. __ ?
#         r.. V...
#     platform_validator ? ?
#
#     r.. l.. u.. __ ?.r.. a.. ?.r__.s.. ?
#
#
# p...
