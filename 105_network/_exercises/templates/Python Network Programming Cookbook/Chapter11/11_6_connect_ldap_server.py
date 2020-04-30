#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 11
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
____ ldap3 ______ Server, Connection, ALL


___ main(address):
    # Create the Server object with the given address.
    # Get ALL information.
    server _ Server(address, get_info_ALL)
    #Create a connection object, and bind with auto bind set to true.
    conn _ Connection(server, auto_bind_True)

    # Print the LDAP Server Information.
    print('******************Server Info**************')
    print(s...info)

    # Print the LDAP Server Detailed Schema.
    print('******************Server Schema**************')
    print(s...schema)

__ _______ __ ______
    parser _ ?.AP..(d.._'Query LDAP Server')
    ?.a_a..('--address', a.._"store", d.._"address",  d.._'ipa.demo1.freeipa.org')
    given_args _ ?.p_a..
    address _ given_args.address
    main (address)

