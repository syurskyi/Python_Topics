from collections.abc ______ Iterable, AsyncIterator
from typing ______ NamedTuple

from curio ______ TaskGroup
______ curio.socket __ socket


c_ Result(NamedTuple):
    domain: s..
    found: bool


@ ___ probe(domain: s..)  Result:
    ___
        await socket.getaddrinfo(domain, N..)
    except socket.gaierror:
        r_ Result(domain, False)
    r_ Result(domain, True)


@ ___ multi_probe(domains: Iterable[s..])  AsyncIterator[Result]:
    @ with TaskGroup() __ group:
        ___ domain __ domains:
            await group.spawn(probe, domain)
        @ ___ task __ group:
            yield task.result
