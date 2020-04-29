# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 5
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
#
# ______ a_p..
# ______ __
# ______ g_p_
# ______ re
# ______ ___
# ______ s_l_
#
# ____ e__.m__.i.. ______ M_I..
# ____ e__.m__.m.. ______ M_M..
# ____ e__.m__.t.. ______ M_T..
#
# SMTP_SERVER _ 'smtp.gmail.com'
# SMTP_PORT _ 587
#
# ___ send_email sender recipient
#     """ Send email message """
#     msg _ M_M..
#     ? 'Subject' _ 'Python Emaill Test'
#     ? 'To' _ r..
#     ? 'From' _ s..
#     subject _ 'Python email Test'
#     message _ 'Images attached.'
#     # attach imgae files
#     files _ __.l_d.. __.g_c..
#     gifsearch _ __.co.. ".gif" __.IG..
#     files _ fi.. ?.s.. f..
#     ___ filename __ ?
#         pa__ _ __.pa__.j.. __.g_c.. ?
#         __ no. __.pa__.i_f.. pa__
#             c..
#         img _ M_I.. o.. pa__ __ .r.. _subtype_"gif"
#         ?.a_h.. 'Content-Disposition', 'attachment' f_n.._f_n..
#         ?.a.. ?
#
#     part _ M_T.. 'text' "plain"
#     ?.s_p.. m..
#     ?.a.. ?
#
#     # create smtp session
#     session _ ?.S.. S_S.. S_P..
#     ?.e..
#     ?.s..
#     ?.e..
#     password _ g_p_.g_p_ prompt_"Enter your Google password: ")
#     ?.l.. s.. p..
#     ?.s_m.. s.. r.. ?.a_s..
#     print ("Email sent.")
#     ?.q..
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'Email Sending Example'
#     ?.a_a.. '--sender'  a.._"store"  d.._"sender"
#     ?.a_a.. '--recipient'  a.._"store"  d.._"recipient"
#     given_args _ ?.p_a..
#     ? ?.s.. ?.r..
