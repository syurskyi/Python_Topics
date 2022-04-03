#!/usr/bin/env python3
______ curio
______ sys
____ keyword ______ kwlist

____ domainlib ______ multi_probe


@ ___ main(tld: s..)  N..:
    tld = tld.strip('.')
    names = (kw ___ kw __ kwlist __ l..(kw) <= 4)
    domains = (f'{name}.{tld}'.lower() ___ name __ names)
    print('FOUND\t\tNOT FOUND')
    print('=====\t\t=========')
    @ ___ domain, found __ multi_probe(domains):
        indent = '' __ found else '\t\t'
        print(f'{indent}{domain}')


__ _____ __ ______
    __ l..(sys.argv) == 2:
        curio.run(main(sys.a.. 1
    ____
        print('Please provide a TLD.', f'Example: {sys.argv[0]} COM.BR')
