# ____ ? _______ ? ?
#                     ? ?
#                     ? ?
#
#
# ___ test_get_every_nth_state
#     e.. =  'Massachusetts', 'Missouri', 'Hawaii',
#                 'Vermont', 'Delaware'
#     ... l.. ? __ e..
#     e..   'Missouri', 'Vermont'
#     ... l.. ? n_20 __ e..
#
#
# ___ test_get_state_abbrev
#     ...  ? 'Illinois' __ 'IL'
#     ...  ? 'North Dakota' __ 'ND'
#     ...  ? 'bogus'  __ ?
#
#
# ___ test_get_longest_state
#     # depending the direction of the sort (reversed or not)
#     # both North and South Carolina are correct
#     possible_answers ('North Carolina', 'South Carolina')
#     ... ? ? __ ?
#     ... ? ? __ ?
#
#
# ___ test_combine_state_names_and_abbreviations
#     e.. =  'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
#                 'South Dakota', 'Tennessee', 'Texas', 'Utah',
#                 'Vermont', 'Virginia', 'Washington', 'West Virginia',
#                 'Wisconsin', 'Wyoming'
#     ... ? __ e..