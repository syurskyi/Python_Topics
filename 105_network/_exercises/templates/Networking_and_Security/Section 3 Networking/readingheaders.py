# #!/usr/bin/python
#
# ______ pc..
# ____ struct ______ _
#
# cap _ ?.o_l.. "eth0", 65536, 1, 0
#
# w__ 1
#     (header, payload) _ cap.n..
#     l2hdr _ p..|;14
#     l2data _ unpack "!6s6sH" ?
#     srcmac _ "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" or. _h.. 0 or. _h.. 1 or. _h.. 2 or. _h.. 3 or. _h.. 4 or. _h.. 5
#     dstmac _ "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" or. _h.. 6 or. _h.. 7 or. _h.. 8 or. _h.. 9 or. _h.. 1 or. _h.. 11
#     print("Source MAC: " ? " Destination MAC: " ?
#
# # get IP header, which is 20 bytes long
# # then unpack it into what it is
#     ipheader _ unpack('!BBHHHBBH4s4s'  p.. 14;34
#     timetolive _ i.. 5
#     protocol _ i.. 6
#     print("Protocol ", st. p.. " Time To Live: ", st. t..
