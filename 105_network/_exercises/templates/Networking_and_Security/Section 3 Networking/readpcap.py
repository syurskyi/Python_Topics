# ______ pc..
# ____ struct ______ _
#
# pcap_file _ pcapy.open_offline("file.pcap")
# count _ 1
#
# w__ ?
#     print("Packet #: " ?
#     ? _ ? + 1
#     header payload _ p__.n..
#     l2hdr _ p.. ;14
#     l2data _ un.. "!6s6sH" ?
#     srcmac _ "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x"  or. _h.. 0 or. _h..1 or. _h.. 2 or. _h.. 3 or. _h.. 4 or. _h.. 5
#     dstmac _ "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x"  or. _h.. 6 or. _h..7 or. _h.. 8 or. _h.. 9 or. _h.. 10 or. _h.. 11
#     print("Source MAC: " ? " Destination MAC: " ?
#
# # get IP header, which is 20 bytes long
# # then unpack it into what it is
#     ipheader _ u.. '!BBHHHBBH4s4s'  p.. 14;34
#     timetolive _ i.. 5
#     protocol _ i.. 6
#     print("Protocol ", st. p.. " Time To Live: ", st. t..
