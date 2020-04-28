#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 11
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


______ a_p..
______ dns.name

___ main(site1, site2):
    _site1 _ dns.name.from_text(site1)
    _site2 _ dns.name.from_text(site2)
    print("site1 is subdomain of site2: ", _site1.is_subdomain(_site2)) 
    print("site1 is superdomain of site2: ", _site1.is_superdomain(_site2)) 
    print("site1 labels: ", _site1.labels)
    print("site2 labels: ", _site2.labels)

__ _______ __ ______
    parser _ ?.AP..(d.._'DNS Python')
    parser.a_a..('--site1', a.._"store", d.._"site1",  default_'www.dnspython.org')
    parser.a_a..('--site2', a.._"store", d.._"site2",  default_'dnspython.org')
    given_args _ parser.p_a..
    site1 _ given_args.site1
    site2 _ given_args.site2
    main (site1, site2)

