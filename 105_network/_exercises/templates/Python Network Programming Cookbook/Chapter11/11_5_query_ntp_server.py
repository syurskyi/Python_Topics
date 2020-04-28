#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 11
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
______ ntplib
____ t__ ______ ctime


___ main(address, v):
    c _ ntplib.NTPClient()
    response _ c.r__(address, version_v)
    print("Response Offset: ", response.offset)
    print("Version: ", response.version)
    print("Response (Time): ", ctime(response.tx_time))
    print("Leap: ", ntplib.leap_to_text(response.leap))
    print("Root Delay: ", response.root_delay)
    print(ntplib.ref_id_to_text(response.ref_id))


__ _______ __ ______
    parser _ ?.AP..(d.._'Query NTP Server')
    ?.a_a..('--address', a.._"store", d.._"address",  default_'pool.ntp.org')
    ?.a_a..('--version', a.._"store", d.._"version",  ty.._in., default_3)
    given_args _ ?.p_a..
    address _ ?.address
    version _ ?.version
    main (address, version)

