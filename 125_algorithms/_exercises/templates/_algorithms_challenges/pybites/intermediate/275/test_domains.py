# _______ p__
#
# ____ ? _______ ? ?
#
#
# ?p__.f.. s.._"module"
# ___ common_domains
#     r.. l.. ?
#
#
# ___ test_get_common_domains common_domains
#     ... l.. ? __ 100
#     first_3 =  'gmail.com', 'yahoo.com', 'hotmail.com'
#     last_3 =  'live.ca', 'aim.com', 'bigpond.net.au'
#     ... ? |3 __ ?
#     ... ? -3| __ ?
#
#
# ?p__.m__.p. "emails, expected", [
#     (["a@gmail.com", "b@pybit.es", "c@pybit.es", "d@domain.de"],
#      [('pybit.es', 2), ('domain.de', 1)]),
#     (["a@hotmail.com", "b@gmail.com"],    # list),
#     (["a@hotmail.com", "b@hotmail.se",
#       "c@paris.com", "d@paris.com", "e@hotmail.it"],
#      [('paris.com', 2), ('hotmail.se', 1)]),
#     (["a@gmail.es", "b@googlemail.com", "c@somedomain.com",
#       "d@somedomain.com", "e@somedomain.com", "f@hotmail.fr"],
#      [('somedomain.com', 3), ('gmail.es', 1)]),
#
# ___ test_get_most_common_domains common_domains emails e..
#     ... ? ? ? __ e..