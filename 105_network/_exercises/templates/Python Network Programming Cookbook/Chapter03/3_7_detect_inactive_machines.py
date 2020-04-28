# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 3
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
# # Requires scapy-2.2.0 or higher for Python 2.7.
# # Visit: http://www.secdev.org/projects/scapy/files/scapy-latest.zip
# # As of now, requires a separate bundle for Python 3.x.
# # Download it from: https://pypi.python.org/pypi/scapy-python3/0.20
#
#
# ______ a_p..
# ______ t__
# ______ sch..
# ____ scapy.all ______ sr, srp, IP, UDP, ICMP, TCP, ARP, Ether
#
# RUN_FREQUENCY _ 10
#
# scheduler _ ?.sc.. t__.t__ t__.s..
#
#
# ___ detect_inactive_hosts scan_hosts
#     """
#     Scans the network to find scan_hosts are live or dead
#     scan_hosts can be like 10.0.2.2-4 to cover range.
#     See Scapy docs for specifying targets.
#     """
#     g.. ?
#     scheduler.enter R.. 1 ?  s_h..
#     inactive_hosts _   # list
#     ___
#         ans, unans _ sr I. d_s_h..)/ICMP r.._0 t.._1
#         ?.su.. l_____ r  ?.sp.. "IP.src is alive"
#         ___ inactive __ u..
#             print ("@ is inactive" ?.ds.
#             i_h_.ap.. ?.ds.
#
#         print ("Total d hosts are inactive" le. i_h..
#
#
#     ______ K..
#         e.. 0
#
#
# __ _____ __ ______
#     parser _ ?.AP.. d.._'Python networking utils'
#     ?.a_a..('--scan-hosts' a.._"store" d.._"scan_hosts" r.._T..
#     given_args _ ?.p_a..
#     scan_hosts _ ?.s_h..
#     s__.e.. 1, 1, ? ?
#     s__.r..

