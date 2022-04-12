# _______ p__
#
# ____ ? _______ ?
#
#
# ___ test_get_profile_no_name
#     w__ p__.r.. T..
#         ... ? )
#
#
# ___ test_get_profile_no_age
#     w__ p__.r.. T..
#         ... ? 'tim'
#
#
# ___ test_get_profile_valueerror
#     w__ p__.r.. V...
#         ... ? 'tim', 'nonint'
#
#
# ___ test_get_profile_too_many_sports
#     w__ p__.r.. V...
#         sports =  'tennis', 'basketball', 'badminton',
#                   'baseball', 'volleyball', 'boxing'
#         ... ? 'tim', 36, $?
#
#
# ___ test_get_profile_dict
#     ... ? 'tim', 36 __ 'name'| 'tim', 'age'| 36
#
#
# ___ test_get_profile_one_sport
#     e.. 'name': 'tim', 'age': 36,
#                 'sports':  'tennis'
#     ... ? 'tim', 36, 'tennis') __ e..
#
#
# ___ test_get_profile_two_sports
#     e.. 'name': 'tim', 'age': 36,
#                 'sports':  'basketball', 'tennis'
#     ... ? 'tim', 36, 'tennis', 'basketball' __ e..
#
#
# ___ test_get_profile_award
#     e.. 'name': 'tim', 'age': 36,
#                 'awards': {'champ': 'helped out team in crisis'
#     ... ? 'tim', 36,
#                        champ='helped out team in crisis' __ e..
#
#
# ___ test_get_profile_two_sports_and_one_award
#     e.. 'name': 'tim', 'age': 36,
#                 'sports':  'basketball', 'tennis' ,
#                 'awards': {'champ': 'helped out team in crisis'
#     ... ? 'tim', 36, 'tennis', 'basketball',
#                        champ='helped out team in crisis' __ e..
#
#
# ___ test_get_profile_two_sports_and_three_awards
#     e.. 'name': 'tim', 'age': 36,
#                 'sports':  'basketball', 'tennis' ,
#                 'awards': {'champ': 'helped out the team in crisis',
#                            'service': 'going the extra mile for our customers',
#                            'attitude': 'unbeatable positive + uplifting'}}
#     ... ? 'tim', 36, 'tennis', 'basketball',
#                        service='going the extra mile for our customers',
#                        champ='helped out the team in crisis',
#                        attitude='unbeatable positive + uplifting') __ e..
