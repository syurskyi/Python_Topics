____ collections.abc ______ Iterable, AsyncIterator
____ typing ______ NamedTuple

____ curio ______ TaskGroup
______ curio.socket __ socket


c_ Result(NamedTuple):
    domain: s..
    found: bool


@ ___ probe(domain: s..)  Result:
    ___
        await socket.getaddrinfo(domain, N..)
    _____ socket.gaierror:
        r_ Result(domain, F..)
    r_ Result(domain, T..)


@ ___ multi_probe(domains: Iterable[s..])  AsyncIterator[Result]:
    @ w__ TaskGroup() __ group:
        ___ domain __ domains:
            await group.spawn(probe, domain)
        @ ___ task __ group:
            yield task.result
