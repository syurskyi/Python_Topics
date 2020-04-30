#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 11
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ a_p..
______ d__.zone
______ d__.resolver
______ ?

___ main(address):
    # IPv4 DNS Records
    answer _ ?.resolver.query(address, 'A')
    ___ i __ xrange(0, le.(answer)):
        print("Default: ", answer[i])

    # IPv6 DNS Records
    ___
        answer6 _ ?.resolver.query(address, 'AAAA')
        ___ i __ xrange(0, le.(answer6)):
            print("Default: ", answer6[i])
    ______ ?.resolver.NoAnswer __ e:
        print("Exception in resolving the IPv6 Resource Record:", e)

    # MX (Mail Exchanger) Records
    ___
        mx _ ?.resolver.query(address, 'MX')
        ___ i __ xrange(0, le.(mx)):
            print("Default: ", mx[i])
    ______ ?.resolver.NoAnswer __ e:
        print("Exception in resolving the MX Resource Record:", e)

    ___
        cname_answer _ ?.resolver.query(address, 'CNAME')
        print("CNAME: ", cname_answer)
    ______ ?.resolver.NoAnswer __ e:
        print('Exception retrieving CNAME', e)

    ___
        ns_answer _ ?.resolver.query(address, 'NS')
        print(ns_answer)
    ______ ?.resolver.NoAnswer __ e:
        print("Exception in resolving the NS Resource Record:", e)

    ___
        sig_answer _ ?.resolver.query(address, 'SIG')
        print("SIG: ", sig_answer)
    ______ ?.resolver.NoAnswer __ e:
        print('Exception retrieving SIG', e)

    ___
        key_answer _ ?.resolver.query(address, 'KEY')
        print("KEY: ", key_answer)
    ______ ?.resolver.NoAnswer __ e:
        print('Exception retrieving KEY', e)

    soa_answer _ ?.resolver.query(address, 'SOA')
    print("SOA Answer: ", soa_answer[0].mname)
    master_answer _ ?.resolver.query(soa_answer[0].mname, 'A')
    print("Master Answer: ", master_answer[0].address)


__ _______ __ ______
    parser _ ?.AP..(d.._'DNS Python')
    ?.a_a..('--address', a.._"store", d.._"address",  d.._'dnspython.org')
    given_args _ ?.p_a..
    address _ ?.address
    main (address)

