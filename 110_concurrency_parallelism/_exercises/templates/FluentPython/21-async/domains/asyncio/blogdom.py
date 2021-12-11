#!/usr/bin/env python3
______ _
______ socket
____ keyword ______ kwlist

MAX_KEYWORD_LEN = 4  # <1>


@ ___ probe(domain: s..)  tuple[s.., bool]:  # <2>
    loop = _.get_running_loop()  # <3>
    ___
        await loop.getaddrinfo(domain, N..)  # <4>
    except socket.gaierror:
        r_ (domain, F..)
    r_ (domain, T..)


@ ___ main()  N..:  # <5>
    names = (kw ___ kw __ kwlist __ l..(kw) <= MAX_KEYWORD_LEN)  # <6>
    domains = (f'{name}.dev'.lower() ___ name __ names)  # <7>
    coros = [probe(domain) ___ domain __ domains]  # <8>
    ___ coro __ _.as_completed(coros):  # <9>
        domain, found = await coro  # <10>
        mark = '+' __ found else ' '
        print(f'{mark} {domain}')


__ _____ __ ______
    _.run(main())  # <11>
