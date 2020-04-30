#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 11
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
# Adopted from http://ldap3.readthedocs.io/tutorial_abstraction_basic.html

____ ldap3 ______ Server, Connection, ObjectDef, AttrDef, Reader, Writer, ALL


___ main
    server _ Server('ipa.demo1.freeipa.org', g_i_A..)
    conn _ Connection(server, 'uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org', 'Secret123', a_b.._T..)
    person _ ObjectDef('person', conn)
    r _ Reader(conn, person, 'ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org')
    print(r)
    print('************')
    person+_'uid'
    print(r)

__ _______ __ ______
    main ()

