#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 11
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
____ ldap3 ______ Server, Connection, ALL, core


___ main(address, dn, password):
    # Create the Server object with the given address.
    server _ Server(address, get_info_ALL)
    #Create a connection object, and bind with the given DN and password.
    ___
        conn _ Connection(server, dn, password, auto_bind_True)
        print('LDAP Bind Successful.')
        # Perform a search for a pre-defined criteria.
        # Mention the search filter / filter type and attributes.
        conn.search('dc=example,dc=com', '(&(uid=euler))' , attributes_['sn'])
        # Print the resulting entries.
        print(conn.entries[0])
    ______ core.exceptions.LDAPBindError __ e:
        # If the LDAP bind failed for reasons such as authentication failure.
        print('LDAP Bind Failed: ', e)

__ _______ __ ______
    parser _ ?.AP..(d.._'Query LDAP Server')
    parser.a_a..('--address', a.._"store", d.._"address",  d.._'ldap.forumsys.com')
    parser.a_a..('--dn', a.._"store", d.._"dn",  d.._'cn=read-only-admin,dc=example,dc=com')
    parser.a_a..('--password', a.._"store", d.._"password",  d.._'password')
    given_args _ parser.p_a..
    address _ ?.address
    dn _ ?.dn
    password _ ?.password
    main (address, dn, password)

