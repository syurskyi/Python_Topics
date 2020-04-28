#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 3
# This program is optimized for Python 3.5.2.
# Instructions to make it run with Python 2.7.x is given below.
# It may run on any other version with/without modifications.

______ __
______ a_p..
______ ?
______ st__
______ se__
______ t__


ICMP_ECHO_REQUEST _ 8 # Platform specific
DEFAULT_TIMEOUT _ 2
DEFAULT_COUNT _ 4


c_ Pinger o..
    """ Pings to a host -- the Pythonic way"""
    
    ___ -  target_host count_D_C.. timeout_D_T..
        ? ?
        ? ?
        ? ?


    ___ do_checksum source_string
        """  Verify the packet integritity """
        sum _ 0
        max_count _ le. ?/2)*2
        count _ 0
        w__ ? < ?

            # To make this program run with Python 2.7.x:            
            # val = ord(source_string[count + 1])*256 + ord(source_string[count])             
            # ### uncomment the above line, and comment out the below line.
            val _ ?|c.. + 1|*256 + ? c..
            # In Python 3, indexing a bytes object returns an integer.
            # Hence, ord() is redundant.            

            s.. _ s.. + ?
            s.. _ s.. & 0xffffffff
            c.. _ c.. + 2
     
        __ m_c.. < le. ?
            s.. _ s.. + or. ?|le. ? - 1
            s.. _ s.. & 0xffffffff
     
        s.. _ s.. >> 16  +  |s.. & 0xffff
        s.. _ s.. + (s.. >> 16)
        answer _ ~s..
        ? _ ? & 0xffff
        ? _ ? >> 8 | (? << 8 & 0xff00)
        r_ ?
 
    ___ receive_pong sock ID timeout
        """
        Receive ping from the socket.
        """
        time_remaining _ t..
        w__ T..
            start_time _ t__.t__
            readable _ se__.se__ s.. || || ?
            time_spent _ t__.t__ - s.._time
            __ r.. 0 __  # Timeout
                r_
     
            time_received _ t__.t__
            recv_packet, addr _ ?.r_f.. 1024
            icmp_header _ ? 20;28
            type, code, checksum, packet_ID, sequence _ st__.u..(
                "bbHHh", icmp_header
            )
            __ packet_ID __ ID
                bytes_In_double _ st__.c_s_ "d"
                time_sent _ st__.u.. "d" r_p.. 28;28 + ? 0
                r_ t_r.. - ?

            time_remaining _ ? - t_s..
            __ ? <_ 0
                r_
     
     
    ___ send_ping sock,  ID
        """
        Send ping to the target host
        """
        target_addr  _  ?.g_h_b_n.. t_h..
     
        my_checksum _ 0
     
        # Create a dummy heder with a 0 checksum.
        header _ st__.pa.. "bbHHh" I_E_R.. 0 ? I. 1
        bytes_In_double _ st__.c_s_ "d"
        data _ (192 - ? * "Q"
        data _ st__.p.. "d" t__.t__ + by.. ?.e.. 'utf-8'
     
        # Get the checksum on the data and the dummy header.
        my_checksum _ d_c.. h.. + d..
        header _ st__.p..(
            "bbHHh", I_E_R.. 0, ?.ht.. m_c.. I. 1
        )
        packet _ h.. + d..
        ?.s_t.. ? t_a.. 1
     
     
    ___ ping_once
        """
        Returns the delay (in seconds) or none on timeout.
        """
        icmp _ ?.g_p_t_n..("icmp")
        ___
            sock _ ?.?(?.A.. ?.SOCK_RAW, icmp)
        ______ ?.e.. __ e:
            __ e.errno __ 1:
                # Not superuser, so operation not permitted
                e.msg +_  "ICMP messages can only be sent from root user processes"
                r_ ?.e..(e.msg)
        ______ E.. __ e:
            print ("Exception: @" (e))
    
        my_ID _ __.g_p.. & 0xFFFF
     
        send_ping(sock, my_ID)
        delay _ receive_pong(sock, my_ID, timeout)
        sock.c..
        r_ delay
     
     
    ___ ping
        """
        Run the ping process
        """
        ___ i __ range(count):
            print ("Ping to @..."  target_host,)
            ___
                delay  _  ping_once()
            ______ ?.g.. __ e:
                print ("Ping failed. (socket error: '@')"  e[1])
                b..
     
            __ delay  __  None:
                print ("Ping failed. (timeout within ssec.)"  timeout)
            ____
                delay  _  delay * 1000
                print ("Get pong in 0.4fms"  delay)

 
 
__ _______ __ ______
    parser _ ?.AP..(d.._'Python ping')
    parser.a_a..('--target-host', a.._"store", d.._"target_host", r.._T..)
    given_args _ parser.parse_args()
    target_host _ given_args.target_host
    pinger _ Pinger(target_host_target_host)
    pinger.ping()
