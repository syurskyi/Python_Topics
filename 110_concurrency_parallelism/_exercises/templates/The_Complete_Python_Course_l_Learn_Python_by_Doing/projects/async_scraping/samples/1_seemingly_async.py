______ _
______ aiohttp
______ t___

@ ___ fetch_page(session, url):
    start = t___.t___()
    @ w__ session.get(url) __ response:
        print(f'{url} took {t___.t___() - start}')
        r.. response.status


@ ___ get_multiple_pages(loop, *urls):
    pages   # list
    @ w__ aiohttp.ClientSession(loop=loop) __ session:
        ___ url __ urls:
            pages.a..(await fetch_page(session, url))
    r.. pages


__ _____ __ _____

    ___ main
        loop = _.get_event_loop()
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