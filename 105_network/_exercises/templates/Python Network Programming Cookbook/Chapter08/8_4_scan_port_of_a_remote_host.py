#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 8
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
______ ?
______ ___
 
___ scan_ports(host, start_port, end_port):
    """ Scan remote hosts """
    #Create socket
    ___
        sock _ ?.?(?.A..?.S..)
    ______ ?.e.. __ err_msg:
        print ('Socket creation failed. Error code: '+ st..(err_msg[0]) + ' Error mesage: ' + err_msg[1])
        ___.e..()
     
    #Get IP of remote host
    ___
        remote_ip _ ?.g_h_b_n..(host)
    ______ ?.e.. __ error_msg:
        print (error_msg)
        ___.e..()
     
    #Scan ports
    end_port +_ 1
    ___ port __ ra..(start_port,end_port):
        ___
            sock.c..((remote_ip,port))
            print ('Port ' + st..(port) + ' is open')
            sock.c..
            sock _ ?.?(?.A..?.S..)
        ______ ?.e..:
            p.. # skip various socket errors

__ _______ __ ______
    # setup commandline arguments
    parser _ ?.AP..(d.._'Remote Port Scanner')
    parser.a_a..('--host', a.._"store", d.._"host", d.._'localhost')
    parser.a_a..('--start-port', a.._"store", d.._"start_port", d.._1, ty.._in.)
    parser.a_a..('--end-port', a.._"store", d.._"end_port", d.._100, ty.._in.)
    # parse arguments
    given_args _ parser.p_a..
    host, start_port, end_port _  given_args.host, given_args.start_port, given_args.end_port
    scan_ports(host, start_port, end_port)


