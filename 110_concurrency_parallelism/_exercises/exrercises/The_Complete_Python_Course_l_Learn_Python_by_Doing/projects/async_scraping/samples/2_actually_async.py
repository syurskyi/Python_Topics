______ asyncio
______ aiohttp
______ t___

async ___ fetch_page(session, url):
    start = t___.t___()
    async with session.get(url) as response:
        print(f'{url} took {t___.t___() - start}')
        r.. response.status


async ___ get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        ___ url __ urls:
            tasks.a..(fetch_page(session, url))
        r.. await asyncio.gather(*tasks)


__ _____ __ _____

    ___ main
        loop = asyncio.get_event_loop()
        urls = [
            'http://google.com',
            'http://example.com',
            'http://tecladocode.com/blog'
        ]
        start = t___.t___()
        pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
        print(f'Total took {t___.t___() - start}')
        ___ page __ pages:
            print(page)

    main()