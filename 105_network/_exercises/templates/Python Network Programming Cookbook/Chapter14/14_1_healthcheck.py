#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 14
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
 
______ ?
____ ___ ______ s_o_
____ t__ ______ sleep
______ a_p..
 
___ is_alive(address, port):
    # Create a socket object to connect with
    s _ ?.?()
    
    # Now try connecting, passing in a tuple with address & port
    ___
        s.c..((address, port))
        r_ T..
    ______ ?.e..:
        r_ F..
    f..
        s.c..
 

___ confirm(addres, port):
    w__ T..:
        __ is_alive(address, port):
            s_o_.write(address + ":" + st..(port) + ' is alive\n')
            s_o_.f..
        ____
            s_o_.write(address + ":" + st..(port) + ' is dead\n')
            s_o_.f..
        sleep(10)


__ _______ __ ______
    # setup commandline arguments
    parser _ ?.AP..(d.._'Health Checker')
    parser.a_a..('--address', a.._"store", d.._"address")
    parser.a_a..('--port', a.._"store", d.._"port", default_80, ty.._in.)
    # parse arguments
    given_args _ parser.parse_args()
    address, port _  given_args.address, given_args.port
    confirm(address, port)


