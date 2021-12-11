______ _
______ socket
____ collections.abc ______ Iterable, AsyncIterator
____ typing ______ NamedTuple, Optional


c_ Result(NamedTuple):  # <1>
    domain: s..
    found: bool


OptionalLoop = Optional[_.AbstractEventLoop]  # <2>


@ ___ probe(domain: s.., loop: OptionalLoop = N..)  Result:  # <3>
    __ loop __ N..:
        loop = _.get_running_loop()
    ___
        await loop.getaddrinfo(domain, N..)
    _____ socket.gaierror:
        r_ Result(domain, F..)
    r_ Result(domain, T..)


@ ___ multi_probe(domains: Iterable[s..])  AsyncIterator[Result]:  # <4>
    loop = _.get_running_loop()
    coros = [probe(domain, loop) ___ domain __ domains]  # <5>
    ___ coro __ _.as_completed(coros):  # <6>
        result = await coro  # <7>
        yield result  # <8>
