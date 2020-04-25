# ______ m.., ___, netaddr, a_p_, l..
# ____ scapy.all ______ *
# ____ d_t_ ______ d_t_
#
# ?.gL.. "scapy.runetime" .sL.. ?.E..
# conf.v.. _ 0
#
#
# c_ const
#     ARP _ 0
#     PING _ 1
#     TCP _ 2
#
#
# ___ arpScan subnet
#     ans, unans _ srp E.. d.._"ff:ff:ff:ff:ff:ff") / ARP pdst_subnet), timeout_2)
#     ___ snd, rcv __ ans
#         print ?.s.. _"[ARP] Online: %ARP.psrc% - %Ether.src%"
#
#
# ___ ping ip
#     reply _ sr1 I. dst_st. ? / ICMP t.._3
#     __ reply __ no. N..
#         print("[PING] Online: " + st. ?
#
#
# ___ tcp ip
#     port _ 53
#     srcp _ RandShort
#     pkt _ sr1 I. dst_st. ? / T.. sport_srcp, dport_port, flags_"S"), t.._5
#     __ ? __ no. N..
#         flag _ ?.g.. T.. .f..
#         __ ? __ 0x12  # syn,ack
#             print("[TCP] Online:" + st. ? + " - replied with syn,ack")
#             s.. I. dst_st. ? / T.. sport_srcp dport_port flags_"R"))
#         ____ flag __ 0x14  # RST
#             print("[TCP] Online: " + st. ? + " - replied with rst,ack")
#
#
# ___ scan subnet typ
#     jobs _   # list
#     ___ ip __ s..
#         __ typ __ c__.P..
#             p _ ?.P.. t.._p.. a.._ ?
#             j__.ap.. ?
#             ?.s..
#         ____
#             p _ ?.P.. t.._t.. a.._ ?
#             j__.ap.. ?
#             ?.s..
#
#     ___ j __ j..
#         ?.j..
#
#
# ___ main args
#     subnet _ n__.I_N.. ?.s..
#     start _ d_t_.n..
#     print("==================================================")
#     print("Scanning " + st. s.. 0 + " to " + st. s.. -1
#     print("Started @ " + st. s..
#     print("==================================================")
#
#     __ ?.scantype __ c__.A..
#         aS.. ?.s..
#     ____ ?.s_t.. __ c__.P..
#         sc.. s.. c__.P..
#     ____ ?.s_t.. __ c__.T..
#         sc.. su.. c__.T..
#     ____
#         aS.. ?.s..
#         s.. su.. c__.P..
#         s.. su.. c__.T..
#
#     stop _ d_t_.now
#     print("==================================================")
#     print("Scan Duration: " + st. s.. - s..
#     print("Completed @ " + st. s..
#     print("==================================================")
#
#
# __ _______ __ _______
#     parser _ a_p_.A_P..
#     ?.a_a.. "subnet", a.._"store", h.._"Subnet to scan for hosts", type_st.
#     ?.a_a.. "scantype", a.._"store", n.._"?", d.._3
#                         h.._"Type of scan: [0 = Arp, 1 = Ping, 2 = TCP, 3 = ALL]", ty.._in.
#
#     __ le. ___.a.. 1; __ 0
#         ?.p_h..
#         ?.e..
#
#     args _ ?.p_a..
#     m.. ?