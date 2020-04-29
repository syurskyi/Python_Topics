#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 8
# This program is optimized for Python 2.7.12.
# It may run on any other version with/without modifications.

______ a_p..
______ pcap
____ construct.protocols.ipstack ______ ip_stack


___ print_packet(pktlen, data, timestamp):
    """ Callback for priniting the packet payload"""
    __ no. data:
        r_
    
    stack _ ip_stack.parse(data)
    payload _ stack.next.next.next
    print (payload)

___ main
    # setup commandline arguments
    parser _ ?.AP..(d.._'Packet Sniffer')
    ?.a_a..('--iface', a.._"store", d.._"iface", d.._'eth0')
    ?.a_a..('--port', a.._"store", d.._"port", d.._80, ty.._in.)
    # parse arguments
    given_args _ ?.p_a..
    iface, port _  given_args.iface, given_args.port
    # start sniffing
    pc _ pcap.pcapObject()
    pc.open_live(iface, 1600, 0, 100)
    pc.setfilter('dst port d' port, 0, 0)
    
    print ('Press CTRL+C to end capture')
    ___
        w__ T..:
            pc.dispatch(1, print_packet)
    ______ K..:
        print ('Packet statistics: d packets received, d packets dropped, d packets dropped by the interface'  pc.stats())

__ _______ __ ______
    main()
        
