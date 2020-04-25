# # Please refer to the commented section below for a short Scapy recap!
#
# # In Scapy, we will use the sniff() function to capture network packets.
# # To see a list of what functions Scapy has available, open Scapy and run the lsc() function.
# # Run the ls() function to see ALL the supported protocols.
# # Run the ls(protocol) function to see the fields and default values for any protocol. E.g. ls(BOOTP)
# # See packet layers and contents with the .show() method.
# # Dig into a specific packet layer using a list index: pkts[3][2].summary()
# # ...the first index chooses the packet out of the pkts list, the second index chooses the layer for that specific packet.
# # Using the .command() method will return a string for the command necessary to recreate that sniffed packet.
#
# # To see the list of optional arguments for the sniff() function:
# # print(sniff.__doc__)
# '''
# Sniff packets and return a list of packets.
#
# Arguments:
#
#   count: number of packets to capture. 0 means infinity.
#
#   store: whether to store sniffed packets or discard them
#
#   prn: function to apply to each packet. If something is returned, it
#       is displayed.
#
#       Ex: prn = lambda x: x.summary()
#
#   filter: BPF filter to apply.
#
#   lfilter: Python function applied to each packet to determine if
#       further action may be done.
#
#       Ex: lfilter = lambda x: x.haslayer(Padding)
#
#   offline: PCAP file (or list of PCAP files) to read packets from,
#       instead of sniffing them
#
#   timeout: stop sniffing after a given time (default: None).
#
#   L2socket: use the provided L2socket (default: use conf.L2listen).
#
#   opened_socket: provide an object (or a list of objects) ready to use
#       .recv() on.
#
#   stop_filter: Python function applied to each packet to determine if
#       we have to stop the capture after this packet.
#
#       Ex: stop_filter = lambda x: x.haslayer(TCP)
#
#   iface: interface or list of interfaces (default: None for sniffing
#       on all interfaces).
#
# The iface, offline and opened_socket parameters can be either an
# element, a list of elements, or a dict object mapping an element to a
# label (see examples below).
#
# Examples:
#
#   >>> sniff(filter="arp")
#
#   >>> sniff(lfilter=lambda pkt: ARP in pkt)
#
#   >>> sniff(iface="eth0", prn=Packet.summary)
#
#   >>> sniff(iface=["eth0", "mon0"],
#   ...       prn=lambda pkt: "@: @" % (pkt.sniffed_on,
#   ...                                   pkt.summary()))
#
#   >>> sniff(iface={"eth0": "Ethernet", "mon0": "Wifi"},
#   ...       prn=lambda pkt: "@: @" % (pkt.sniffed_on,
#   ...                                   pkt.summary()))
# '''
#
# # Importing the necessary modules
# ______ l..
# ____ d_t_ ______ d_t_
# ______ su..
# ______ ___
#
# # This will suppress all messages that have a lower level of seriousness than error messages, while running or loading Scapy
# ?.gL.. "scapy.runtime").sL..(?.E..)
# ?.gL.. "scapy.interactive").sL..(?.E..)
# ?.gL.. "scapy.loading").sL..(?.E..)
#
# ___
#     ____ scapy.all ______ _
#
# ______ I..
#     print("Scapy package for Python is not installed on your system.")
#     ___.e..
#
# # Printing a message to the user; always use "sudo scapy" in Linux!
# print("\n! Make sure to run this program as ROOT !\n")
#
# # Asking the user for some parameters: interface on which to sniff, the number of packets to sniff, the time interval to sniff, the protocol
#
# # Asking the user for input - the interface on which to run the sniffer
# net_iface _ in__("* Enter the interface on which to run the sniffer (e.g. 'enp0s8'): ")
#
# # Setting network interface in promiscuous mode
# '''
# Wikipedia: In computer networking, promiscuous mode or "promisc mode"[1] is a mode for a wired network interface controller (NIC) or wireless network interface controller (WNIC) that causes the controller to pass all traffic it receives to the central processing unit (CPU) rather than passing only the frames that the controller is intended to receive.
# This mode is normally used for packet sniffing that takes place on a router or on a computer connected to a hub.
# '''
# ___
#     ?.ca.. "ifconfig" ? "promisc"|, s_o.._N.. s_e.._N.. sh.._F..
#
# ______
#     print("\nFailed to configure interface as promiscuous.\n")
#
# ____
#     # Executed if the try clause does not raise an exception
#     print("\nInterface @ was set to PROMISC mode.\n"  ?
#
# # Asking the user for the number of packets to sniff (the "count" parameter)
# pkt_to_sniff _ in__("* Enter the number of packets to capture (0 is infinity): ")
#
# # Considering the case when the user enters 0 (infinity)
# __ in. ? !_ 0
#     print("\nThe program will capture d packets.\n"  in. ?
#
# ____ in. ? __ 0
#     print("\nThe program will capture packets until the timeout expires.\n")
#
# # Asking the user for the time interval to sniff (the "timeout" parameter)
# time_to_sniff _ in__("* Enter the number of seconds to run the capture: ")
#
# # Handling the value entered by the user
# __ in. ? !_ 0
#     print("\nThe program will capture packets for %d seconds.\n"  in. ?
#
# # Asking the user for any protocol filter he might want to apply to the sniffing process
# # For this example I chose three protocols: ARP, BOOTP, ICMP
# # You can customize this to add your own desired protocols
# proto_sniff _ in__("* Enter the protocol to filter by (arp|bootp|icmp|0 is all): ")
#
# # Considering the case when the user enters 0 (meaning all protocols)
# __ ? __ "arp" o.  ? __ "bootp" o. ? __ "icmp"
#     print("\nThe program will capture only @ packets.\n"  ?.u..
#
# ____ ? __ "0"
#     print("\nThe program will capture all protocols.\n")
#
# # Asking the user to enter the name and path of the log file to be created
# file_name _ in__("* Please give a name to the log file: ")
#
# # Creating the text file (if it doesn't exist) for packet logging and/or opening it for appending
# sniffer_log _ o.. ? _
#
#
# # This is the function that will be called for each captured packet
# # The function will extract parameters from the packet and then log each packet to the log file
# ___ packet_log packet
#     # Getting the current timestamp
#     now _ d_t_.n..
#
#     # Writing the packet information to the log file, also considering the protocol or 0 for all protocols
#     __ proto_sniff __ "0"
#         # Writing the data to the log file
#         print("Time: " + st. ? + " Protocol: ALL" + " SMAC: " + pa.. 0 .sr. + " DMAC: " + pa..  0 .ds.
#               file_sniffer_log
#
#     ____ ? __ "arp" o. ? __ "bootp" o. ? __ "icmp"
#         # Writing the data to the log file
#         print(
#             "Time: " + st. ? + " Protocol: " + ?.u.. + " SMAC: " + pa.. 0 .sr. + " DMAC: " + pa..
#                 0].ds. f_s_l..
#
#
# # Printing an informational message to the screen
# print("\n* Starting the capture...")
#
# # Running the sniffing process (with or without a filter)
# __ proto_sniff __ "0"
#     sn.. i_n_i.. c_i. p_t_s.. t_i.. t_t_s.. p_p_l..
#
# ____ ? __ "arp" o. ? __ "bootp" o. ? __ "icmp"
#     s.. i_n_i.. f_p_s.. c_i.. p_t_s.. t_i. t_t_s.. p_p_l..
#
# ____
#     print("\nCould not identify the protocol.\n")
#     ___.e..
#
# # Printing the closing message
# print("\n* Please check the @ file to see the captured packets.\n"  f_n..
#
# # Closing the log file
# ?.c..
#
# # End of the program.
# # Feel free to modify it, test it, add new protocols to sniff and improve de code whenever you feel the need to.