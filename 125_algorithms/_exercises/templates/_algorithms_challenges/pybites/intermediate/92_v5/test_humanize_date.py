# ____ d__ _______ t..
#
# _______ p__
#
# ____ ? _______ ? ?
#
#
# ___ n_days_ago_str days
#     r..  N.. - t.. d.._d__.s.. _m/_d/_y
#
#
# ?p__.m__.p. "arg, expected"
#      N.. - t.. s.._2), 'just now'
#      N.. - t.. s.._9), 'just now'
#      N.. - t.. s.._10), '10 seconds ago'
#      N.. - t.. s.._59), '59 seconds ago'
#      N.. - t.. m.._1), 'a minute ago'
#      N.. - t.. m.._1, s.._40), 'a minute ago'
#      N.. - t.. m.._2), '2 minutes ago'
#      N.. - t.. m.._59), '59 minutes ago'
#      N.. - t.. h.._1), 'an hour ago'
#      N.. - t.. h.._2), '2 hours ago'
#      N.. - t.. h.._23), '23 hours ago'
#      N.. - t.. h.._24), 'yesterday'
#      N.. - t.. h.._47), 'yesterday'
#      N.. - t.. d.._1), 'yesterday'
#      N.. - t.. d.._2), ?(2,
#      N.. - t.. d.._7), ?(7,
#      N.. - t.. d.._100), ?(100,
#      N.. - t.. d.._365), ?(365,
#
# ___ test_pretty_date arg e..
#     ... ? ? __ e..
#
#
# ___ test_input_variable_of_wrong_type
#     w__ p__.r.. V...
#         ? 123
#
#
# ___ test_input_variable_future_date
#     w__ p__.r.. V...
#         ? N.. + t.. d.._1