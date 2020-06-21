# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 5
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ s_l_
# ______ e__.u..
# ______ a_p..
# ____ e__.m__.text ______ M_T..
#
# ___ mail_client host port fromAddress toAddress subject body
#     msg _ M_T..(body)
#     ? 'To' _ e__.u__.f_a.. 'Recipient' tA..
#     ? 'From' _ e__.u__.f_a.. 'Author' fA..
#     ? 'Subject' _ ?
#
#     server _ s_l_.S.. ? ?
#     s...s_d.. T..
#     ___
#         s...s_m.. fA.. tA.. ?.a_s..
#     f..
#         s...q..
#
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'Mail Server Example'
#     ?.a_a.. '--host' a.._"store" d.._"host" ty.._str r.._T..
#     ?.a_a.. '--port' a.._"store" d.._"port" ty.._in. r.._T..
#     ?.a_a.. '--fromAddress' a.._"store" d.._"fromAddress" ty.._str r.._T..
#     ?.a_a.. '--toAddress' a.._"store" d.._"toAddress" ty.._str r.._T..
#     ?.a_a.. '--subject' a.._"store" d.._"subject" ty.._str r.._T..
#     ?.a_a.. '--body' a.._"store" d.._"body" ty.._str r.._T..
#     given_args _ ?.p_a..
#     ? ?.h.. ?.p.. ?.fA.. ?.tA.. ?.s.. ?.b..
#
