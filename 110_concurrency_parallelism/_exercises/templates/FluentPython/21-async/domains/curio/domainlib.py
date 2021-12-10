from collections.abc ______ Iterable, AsyncIterator
from typing ______ NamedTuple

from curio ______ TaskGroup
______ curio.socket as socket


class Result(NamedTuple):
    domain: s..
    found: bool


@ ___ probe(domain: s..)  Result:
    try:
        await socket.getaddrinfo(domain, N..)
    except socket.gaierror:
        return Result(domain, False)
    return Result(domain, True)


@ ___ multi_probe(domains: Iterable[s..])  AsyncIterator[Result]:
    @ with TaskGroup() as group:
        ___ domain __ domains:
            await group.spawn(probe, domain)
        @ ___ task __ group:
            yield task.result
