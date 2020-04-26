# ______ ___, a_p_, so.., m.., su.., t__
# ____ d_t_ ______ d_t_
#
#
# ___ scan ip port
#     ___
#         s _ ?.? ?.A.. ?.S..
#         s.s_t.. 2.0
#         res _ ?.c_e. ?
#         __ ?__ 0
#             __ port __ 80:
#                 rsp _ "HEAD / HTTP/1.1\r\nhost: " + i. + "\r\n\r\n"
#                 s.s.. ?.en..
#             banner _ s.r.. 4096
#             msg _ "[+] Port " + st. p.. + " open\n"
#             ? +_ "------------------------\n" + b__.st__.d..
#             print ? + "\n------------------------\n")
#         s.c..
#     ______ ?.t_o..
#         banner _ "No Banner Message"
#         __ port __ 53
#             banner _ ?.g_o..("nslookup -type=any -class=chaos version.bind " + i.
#         msg _ "[+] Port " + st. p.. + " open\n"
#         ? +_ "------------------------\n" + b__.s__.d..
#         print ? + "\n------------------------\n")
#         s.c..
#
#
# ___ main args
#     ___
#         ?.t.. _ fl.. ?.t..
#         start _ d_t_.n..
#         print("==================================================")
#         print("Scanning " + ?.I. + " Ports: " + st. ?.s.. + " - " + st. ?.e..
#         print("==================================================\n")
#         ports _ ra.. ?.s.. ?.e.. + 1
#         ___ port __ ?
#             p _ ?.P.. t.._? a.._ ?.I. p..
#             ?.s..
#             t__.s.. ?.th..
#         t__.s.. 3
#         stop _ d_t_.n..
#         print("==================================================")
#         print("Scan Duration: " + st. s.. - s..
#         print("==================================================")
#     ______ E.. __ err
#         print st.?
#
#
# __ _______ __ _______
#     parser _ a_p_.A_P..
#     ?.a_a.. "IP" a.._"store" h.._"IP to scan" ty.._st.
#     ?.a_a.. "sport" a.._"store" n.._"?" d.._1 h.._"Starting port range" ty.._in.
#     ?.a_a.. "eport" a.._"store" n.._"?" d.._1024 h.._"End port range" ty.._in.
#     ?.a_a.. "-t" "--throttle" a.._"store" h.._"throttle connection attempts"
#                         n.._"?" d.._0.25 c.._0.05
#
#     __ le.(___.a.. 1; __ 0
#         ?.p_h..
#         ?.e..
#
#     args _ ?.p_a..
#     m.. ?