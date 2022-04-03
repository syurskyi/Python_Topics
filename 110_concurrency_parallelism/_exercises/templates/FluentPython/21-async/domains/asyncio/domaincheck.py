#!/usr/bin/env python3
______ _
______ sys
____ keyword ______ kwlist

____ domainlib ______ multi_probe


@ ___ main(tld: s..)  N..:
    tld = tld.strip('.')
    names = (kw ___ kw __ kwlist __ l..(kw) <= 4)  # <1>
    domains = (f'{name}.{tld}'.lower() ___ name __ names)  # <2>
    print('FOUND\t\tNOT FOUND')  # <3>
    print('=====\t\t=========')
    @ ___ domain, found __ multi_probe(domains):  # <4>
        indent = '' __ found else '\t\t'  # <5>
        print(f'{indent}{domain}')


__ _____ __ ______
    __ l..(sys.argv) == 2:
        _.run(main(sys.a.. 1   # <6>
    ____
        print('Please provide a TLD.', f'Example: {sys.argv[0]} COM.BR')
