#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 11
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
______ d__.zone
______ d__.resolver
______ ?

___ main(address):
    soa_answer _ ?.resolver.query(address, 'SOA')
    master_answer _ ?.resolver.query(soa_answer[0].mname, 'A')
    ___
        z _ ?.zone.from_xfr(?.query.xfr(master_answer[0].address, address))
        names _ z.nodes.keys()
        names.sort()
        ___ n __ names:
            print(z[n].to_text(n))
    ______ ?.e.. __ e:
        print('Failed to perform zone transfer:', e)
    ______ d__.exception.FormError __ e:
        print('Failed to perform zone transfer:', e)


__ _______ __ ______
    parser _ ?.AP..(d.._'DNS Python')
    ?.a_a..('--address', a.._"store", d.._"address",  d.._'dnspython.org')
    given_args _ ?.p_a..
    address _ ?.address
    main (address)

