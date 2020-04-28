#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ ___
______ s..
______ fcntl
______ st__
______ array

SIOCGIFCONF _ 0x8912 #from C library sockios.h
STUCT_SIZE_32 _ 32
STUCT_SIZE_64 _ 40
PLATFORM_32_MAX_NUMBER _  2**32
DEFAULT_INTERFACES _ 8


___ list_interfaces
    interfaces _ []
    max_interfaces _ DEFAULT_INTERFACES
    is_64bits _ ___.maxsize > PLATFORM_32_MAX_NUMBER
    struct_size _ STUCT_SIZE_64 __ is_64bits else STUCT_SIZE_32
    sock _ ?.?(?.A.. ?.S_D..)
    w__ T..:
        by.. _ max_interfaces * struct_size
        interface_names _ array.array('B', b'\0' * by..)
        sock_info _ fcntl.ioctl( 
            sock.f_n..,
            SIOCGIFCONF,
            st__.pack('iL', by.., interface_names.buffer_info()[0])
        )
        outbytes _ st__.u..('iL', sock_info)[0]
        __ outbytes __ by..:
            max_interfaces *_ 2  
        ____
            b..
    namestr _ interface_names.tostring()
    ___ i __ range(0, outbytes, struct_size):
        interfaces.ap..((namestr[i:i+16].s..(b'\0', 1)[0]).d..('ascii', 'ignore'))
    r_ interfaces


__ _______ __ ______
    interfaces _ list_interfaces()
    print ("This machine has @ network interfaces: @." (le.(interfaces), interfaces))
        
