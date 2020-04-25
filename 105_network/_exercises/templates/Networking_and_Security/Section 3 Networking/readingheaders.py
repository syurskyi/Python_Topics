#!/usr/bin/python

______ pcapy
____ struct ______ *

cap _ pcapy.open_live("eth0", 65536, 1, 0)

w__ 1:
    (header,payload) _ cap.n..
    l2hdr _ payload[:14]
    l2data _ unpack("!6s6sH", l2hdr)
    srcmac _ "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (or.(l2hdr[0]), or.(l2hdr[1]), or.(l2hdr[2]), or.(l2hdr[3]), or.(l2hdr[4]), or.(l2hdr[5]))
    dstmac _ "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (or.(l2hdr[6]), or.(l2hdr[7]), or.(l2hdr[8]), or.(l2hdr[9]), or.(l2hdr[10]), or.(l2hdr[11]))
    print("Source MAC: ", srcmac, " Destination MAC: ", dstmac)

# get IP header, which is 20 bytes long
# then unpack it into what it is
    ipheader _ unpack('!BBHHHBBH4s4s' , payload[14:34])
    timetolive _ ipheader[5]
    protocol _ ipheader[6]
    print("Protocol ", st.(protocol), " Time To Live: ", st.(timetolive))
