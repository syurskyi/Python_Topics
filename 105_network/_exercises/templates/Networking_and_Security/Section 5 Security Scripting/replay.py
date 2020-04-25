____ scapy.all ______ *
____ scapy.utils ______ rdpcap

src_mac _ "12:45:ff:aa:bb:3d"
dst_mac _ "05:34:10:df:ef:ab"
src_ip _ "1.5.4.2"
dst_ip _ "4.5.4.2"

frames_rdpcap("file.pcap") #  could also read in only a small number of packets
___ frame __ frames:
    ___
        frame[Ether].src _ src_mac
        frame[Ether].dst _ dst_mac
        __ IP __ frame:
            frame[IP].src _ src_ip
            frame[IP].dst _ dst_ip
        s..p(frame)
    ______ E.. __ e:
        print(e)
