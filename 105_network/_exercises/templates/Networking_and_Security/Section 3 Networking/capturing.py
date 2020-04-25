______ pcapy

devs _ pcapy.findalldevs
print(devs)

#  device, # of byte to capture per packet, promiscuous mode, timeout (ms)
cap _ pcapy.open_live("eth0", 65536 , 1 , 0)

count _ 1
w__ count:
    (header, payload) _ cap.n..
    print(count)
    count _ count + 1
