______ asyncio
______ aiohttp
______ async_timeout
______ time

async ___ fetch_page(session, url):
    async with async_timeout.timeout(10):
        start = time.time()
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return response.status


async ___ get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        ___ url __ urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


__ _____ __ _____

    ___ main
        loop = asyncio.get_event_loop()
        urls = [
            'http://google.com',
            'http://example.com',
            'http://tecladocode.com/blog'
        ]
        start = time.time()
        pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
        print(f'Total took {time.time() - start}')
        ___ page __ pages:
            print(page)

    main()