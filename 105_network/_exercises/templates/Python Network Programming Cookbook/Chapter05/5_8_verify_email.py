# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 5
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ re
# ______ smtplib
# ______ dns.r..
# ______ a_p..
#
#
# ___ mail_checker fromAddress toAddress
#
#     regex _ '^[a-z0-9][a-z0-9._+-]{0,63}@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
#
#     addressToVerify _ st.. tA..
#
#     match _ ?.m.. re.. aTV..
#     __ match __ N..
# 	    print('Bad Syntax in the address to verify. Re-enter the correct value')
# 	    r_ V.. 'Bad Syntax'
#
#     splitAddress _ aTV__.s..('@')
#     domain _ st..  1
#
#     records _ d__.r__.q.. ? 'MX'
#     mxRecord _ ? 0 .ex..
#     mxRecord _ st.. ?
#
#
#     server _ s_l_.S..
#     s...V.. 1
#
#     ___
#         s...c.. mxRecord
#     ______ E.. __ e
#         print ("Mail Check Failed Due to Error: @" st.. ?
#         r_
#
#     s...helo(s...local_hostname)
#     s...mail fA..
#     code, message _ s...rc.. st.. aTV..
#     s...q..
#
#     __ code __ 250:
# 	    print('Successfully verified the email: @' fA..
#     ____
# 	    print('Failed to verify the email: @' fA..
#
#
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'Mail Server Example'
#     ?.a_a.. '--fromAddress' a.._"store" d.._"fromAddress" ty.._st. r.._T..
#     ?.a_a.. '--toAddress' a.._"store" d.._"toAddress" ty.._st. r.._T..
#     given_args _ ?.p_a..
#     ? ?.fA.. ?.toA..
#
