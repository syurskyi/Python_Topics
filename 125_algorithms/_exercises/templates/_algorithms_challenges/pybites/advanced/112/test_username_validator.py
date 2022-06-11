# ____ t___.__ _______ Pattern
#
# _______ p__
#
# ____ ? _______ (V..
#                                 p..
#                                 v..
#
#
# ___ test_parse_social_platforms_string
#     platforms ?
#     ... l.. ? __ 3
#     ... a.. t..(nw) __ V.. ___ nw __ ?.v..
#     twitter ?.g.. 'Twitter'
#     ... t.. ?.r.. __ r..  # range upper limit = exclusive!
#     ... isi.. ?.r.. P..  # nope, no regex here ;)
#
#
# ___ test_validate_username_wrong_validator
#     w__ p__.r.. V...
#         ? Github bob
#
#
# ___ test_validate_username_twitter_range
#     ... ? 'Twitter', 'a'
#     ... n.. ? 'Twitter', ''
#     ... n.. ? 'Twitter', 'a'*16
#
#
# ___ test_validate_username_twitter_regex
#     ... ? 'Twitter', 'bob'
#     ... ? 'Twitter', 'boB123'
#     ... ? 'Twitter', 'bo__89A'
#     ... n.. ? 'Twitter', 'bob-123'
#     ... n.. ? 'Twitter', 'bob@PyBites'
#     ... n.. ? 'Twitter', 'bob.'
#
#
# ___ test_validate_username_facebook_range
#     ... ? 'Facebook', 'abc123'
#     ... n.. ? 'Facebook', 'bob'
#     ... n.. ? 'Facebook', 'a'*51
#
#
# ___ test_validate_username_facebook_regex
#     ... ? 'Facebook', 'bobb.'
#     ... ? 'Facebook', 'bob.PyBites'
#     ... ? 'Facebook', 'aAbB123'
#     ... n.. ? 'Facebook', 'bobb,'
#     ... n.. ? 'Facebook', 'bob$56'
#     ... n.. ? 'Facebook', 'bob123_'
#
#
# ___ test_validate_username_reddit_range
#     ... ? 'Reddit', 'abc'
#     ... n.. ? 'Reddit', 'ab'
#     ... n.. ? 'Reddit', 'a'*21
#
#
# ___ test_validate_username_reddit_regex
#     ... ? 'Reddit', 'bob_PyBites'
#     ... ? 'Reddit', '-123ABC'
#     ... ? 'Reddit', '123-abc__'
#     ... n.. ? 'Reddit', 'bobb.'
#     ... n.. ? 'Reddit', 'bob@PyBites'
#     ... n.. ? 'Reddit', 'bob$56'