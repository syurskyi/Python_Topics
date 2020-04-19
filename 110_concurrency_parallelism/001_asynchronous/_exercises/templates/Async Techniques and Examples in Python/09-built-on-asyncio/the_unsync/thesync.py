___ un.. ______ un..
______ a..
______ da..
______ ma..

______ ai..
______ re..


___ main
    t0 _ d_t_.d_t_.n..

    tasks _ [
        compute_some(),
        compute_some(),
        compute_some(),
        download_some(),
        download_some(),
        download_some_more(),
        download_some_more(),
        wait_some(),
        wait_some(),
        wait_some(),
        wait_some(),
    ]

    [t.result() for t in tasks]

    dt _ d_t_.d_t_.n.. - t0
    print("Synchronous version done in {:,.2f} seconds.".format(dt.total_seconds()))


@unsync(cpu_bound_True)
___ compute_some():
    print("Computing...")
    for _ in range(1, 10_000_000):
        math.sqrt(25 ** 25 + .01)


@unsync()
async ___ download_some():
    print("Downloading...")
    url _ 'https://talkpython.fm/episodes/show/174/coming-into-python-from-another-industry-part-2'
    async with aiohttp.ClientSession(connector_aiohttp.TCPConnector(ssl_False)) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()

            text _ await resp.text()

    print("Downloaded (more) {:,} characters.".format(len(text)))


@unsync()
___ download_some_more():
    print("Downloading more ...")
    url _ 'https://pythonbytes.fm/episodes/show/92/will-your-python-be-compiled'
    resp _ requests.get(url)
    resp.raise_for_status()

    text _ resp.text

    print("Downloaded {:,} characters.".format(len(text)))


@unsync()
async ___ wait_some():
    print("Waiting...")
    for _ in range(1, 1000):
        await asyncio.sleep(.001)


__ _________ __ ________
    ?
