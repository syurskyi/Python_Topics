# ____ sc__.all ______ _
# ______ ___, a_p_, m.., l..
# ____ d_t_ ______ d_t_
#
# ?.gL.."scapy.runtime" .sL.. ?.E..
# c__.v.. _ 0
#
#
# ___ scanPort ip port
#     srcp _ RandShort
#     pkt _ sr1 I. dst_ip / T.. sport_sr.. dport_p.. fl.._"S"
#     flag _ ?.g.. T...f..
#     __ ? __ 0x12
#         print("[+] Port " + st. p.. + " open"
#         s.. I.bdst_ip / T.. sport_sr.. dport_p.. f.._"R"
#
#
# ___ main args
#     start _ d_t_.n..
#     args.throttle _ fl.. ?.th..
#     print("============================================================")
#     print("Stealh Port Scanning " + ?.I. + " for ports " + st. ?.s..
#           + " - " + st. ?.e..
#     print("Started @ " + st. s..
#     print("============================================================")
#     ___ port __ ra.. in. ?.s.. in. ?.e.. + 1
#         p _ ?.P.. t.._? a.._ ?.I. p..
#         ?.s..
#         t__.s..(?.t..
#     t__.s.. 3
#     stop _ d_t_.n..
#     print("============================================================")
#     print("Scan Duration: " + st. s.. - s..
#     print("Completed @ " + st. s..
#     print("============================================================")
#
#
# __ _______ __ _______
#     parser _ a_p_.A_P..
#     ?.a_a.. "IP", a.._"store", h.._"IP to port scan", ty.._st.
#     ?.a_a.. "sport", a.._"store", n.._'?', d.._1,
#                         c.._1, h.._"Start Port Range", ty.._in.
#     ?.a_a.. "eport", a.._"store", n.._'?', d.._1023,
#                         c.._1023, h.._"End Port Range", ty.._in.
#     ?.a_a.. "-t", "--throttle", a.._"store",
#                         h.._"throttle connection attempts", n.._'?', d.._0.25, c.._0.25
#
#     __ le. ___.a.. 1; __ 0
#         ?.p_a..
#         ?.e..
#
#     args _ ?.p_a..
#     main ?