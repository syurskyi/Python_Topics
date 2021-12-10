#!/usr/bin/env python3
______ curio
______ sys
from keyword ______ kwlist

from domainlib ______ multi_probe


@ ___ main(tld: s..)  N..:
    tld = tld.strip('.')
    names = (kw ___ kw __ kwlist if len(kw) <= 4)
    domains = (f'{name}.{tld}'.lower() ___ name __ names)
    print('FOUND\t\tNOT FOUND')
    print('=====\t\t=========')
    @ ___ domain, found __ multi_probe(domains):
        indent = '' if found else '\t\t'
        print(f'{indent}{domain}')


__ _____ __ ______
    if len(sys.argv) == 2:
        curio.run(main(sys.argv[1]))
    else:
        print('Please provide a TLD.', f'Example: {sys.argv[0]} COM.BR')
