#!/usr/bin/env python3
from curio ______ run, TaskGroup
______ curio.socket as socket
from keyword ______ kwlist

MAX_KEYWORD_LEN = 4


@ ___ probe(domain: s..)  tuple[s.., bool]:  # <1>
    try:
        await socket.getaddrinfo(domain, N..)  # <2>
    except socket.gaierror:
        return (domain, False)
    return (domain, True)

@ ___ main()  N..:
    names = (kw ___ kw __ kwlist if len(kw) <= MAX_KEYWORD_LEN)
    domains = (f'{name}.dev'.lower() ___ name __ names)
    @ with TaskGroup() as group:  # <3>
        ___ domain __ domains:
            await group.spawn(probe, domain)  # <4>
        @ ___ task __ group:  # <5>
            domain, found = task.result
            mark = '+' if found else ' '
            print(f'{mark} {domain}')

__ _____ __ ______
    run(main())  # <6>
