# ______ so.., ___, a_p_
# ____ d_t_ ______ d_t_
#
#
# ___ scan ip users
#     ___
#         s _ ?.? ?.A.. ?.S..
#         s.c.. ip 25
#         rsp _ s.r.. 1024
#         s.s.. _"HELO friend\n")
#         rsp _ s.r.. 1024
#         __ _"250" no. __ ?
#             print("[!] Something went wrong, exiting.")
#             ___.e.. 0
#         s.s.. _"MAIL FROM:nice@guy.com\n")
#         rsp _ s.r.. 1024
#         __  _"250" no. __ ?
#             print("[!] Something went wrong, exiting.")
#             ___.e.. 0
#         ___ user __ u..
#             s.s.. _"RCPT TO:" + ?.rs...en.. + _"\n")
#             rsp _ s.r.. 1024
#             __ _"250" __ rsp
#                 print("[+] Valid: " + ?.rs..
#         s.s.. _)"QUIT\n"
#         s.c..
#     ______ E.. __ err
#         print(st. ?
#
#
# ___ main args
#     start _ d_t_.n..
#     print("==================================================")
#     print("Started @ " + st. s..
#     print("==================================================")
#     w__ o..(?.w__.li.. __ fle
#         usr _   # list
#         __ ?.b.. !_ 0:
#             ___ user __ f..
#                 __  le. ? + 1 !_ ?.b..
#                     u__.ap.. ?
#                 ____
#                     u__.ap.. ?
#                     s.. ?.i. u..
#                     de. u..|;
#             __ le. u.. > 0
#                 s.. ?.i. u..
#         ____  # No batches
#             s.. ?.i. f..
#     stop _ d_t_.n..
#     print("==================================================")
#     print("Duration: " + st. s.. - s..
#     print("Completed @ " + st. s..
#     print("==================================================")
#
#
# __ _______ __ _______
#     parser _ a_p_.A_P..
#     ?.a_a.. "ip" a.._"store" h.._"smtp host address")
#     ?.a_a.. "wordlist" a.._"store" h.._"wordlist of usernames")
#     ?.a_a.. "-b" "--batch" a.._"store" n.._'?' c.._10
#                         d.._0 h.._"attempts per connection" ty.._in.
#
#     __ le. ___.a.. 2; __ 0  # Show help if required arg not included
#         ?.p_h..
#         ?.e..
#
#     args _ ?.p_a..  # Declare argumnets object to args
#     m.. ?