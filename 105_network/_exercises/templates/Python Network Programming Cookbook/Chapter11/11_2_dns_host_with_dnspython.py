#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 11
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


______ a_p..
______ dns.reversename
______ dns.resolver

___ main(address):
    n _ dns.reversename.from_address(address)
    print(n)
    print(dns.reversename.to_address(n))

    ___
        # Pointer records (PTR) maps a network interface (IP) to the host name.
        domain _ st..(dns.resolver.query(n,"PTR")[0])
        print(domain)
    ______ E.. __ e:
        print ("Error while resolving @: @" (address, e))


__ _______ __ ______
    parser _ ?.AP..(d.._'DNS Python')
    parser.a_a..('--address', a.._"store", d.._"address",  default_'127.0.0.1')
    given_args _ parser.p_a..
    address _ given_args.address
    main (address)

