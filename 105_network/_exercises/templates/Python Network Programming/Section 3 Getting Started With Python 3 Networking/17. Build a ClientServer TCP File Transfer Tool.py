# ______ __ a_p_ so.. s_s.. bin__cii
#
# c_ tcpServer s_s_.BRH..
#     ___ handle
#         data _ re__.r.. 512 .st..
#         __ ?.s_w_ _"send:"
#             fle _ ?.sp.. _":" 1
#             print("Receiving File: " + ?.d..
#             w__ o.. st. ?.d.. "utf-8" __ __ f
#                 w__ d..
#                     d.. _ b_a.. re__.r.. 512 .st..
#                     __ le. ?  2 __ 0
#                         f.w.. b_a_.u.. ?
#                     ____
#                         f.w..(b_a_.u.. ?.ap.. 0
#         print ("File Received.\n-----------------------------------")
#
# ___ startServer args
#     server _ s_s_.T_S_ "" ?.po.. ?
#     print "[Server Started]"
#     ?.s_f..
#
# ___ startClient args
#     sock _ ?.? ?.A.. ?.S..
#     ?.c.. ?.i. ?.p..
#     pa__, fle _ __.pa__.sp.. ?.f..
#     print("Sending file: " + ?.f..
#     ?.s_a.. _"send:" + by.. f.. "utf-8"
#     w__ o.. ?.f.. __ __ f
#         data _ f.r.. 512
#         w__ ?
#             ?.s_a.. b_a_.h.. ?
#             data _ f.r.. 512
#     ?.c..
#     print("File sent: " + ?.f..
#
#
# ___ main args
#     __ ?.c..
#         sC.. ?
#     ____ ?.s..
#         ? ?
#
# __ _______ __ _______
#     parser _ a_p_.A_P..
#     ?.a_a.. -c" --client" a.._ store" h.._ start client" ty.._st.
#     nargs_'?', d.._F.. c.._T..
#     ?.a_a..  -s" --server" a.._ store" h.._ start server" ty.._st.
#     nargs_'?' d.._F.. c.._T..
#     ?.a_a.. -i" --ip" a.._"store", h.._ remote server ip" ty.._st.
#     ?.a_a.. -p" --port", a.._"store", h.._ remote server port" ty.._in.
#     ?.a_a.. -f" --file", a.._"store", h.._ file to send" ty.._st.
#
#     args _ ?.p_a.. # Declare argumnets object to args
#     __ no. ?.c.. an. no. ?.s..
#         ?.p_h..
#         print ("\n\nYou must specify --client or --server")
#         ?.e..
#     m.. ?