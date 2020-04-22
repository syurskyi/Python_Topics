______ a..
______ ai..

? ___ get_html(session, url):
    ? w__ session.get(url) as res:
        r_ await res.text()

? ___ main():
    urls _ [
        'http://python.org',
        'http://google.com',
        ''
    ]

    ? w__ ?.ClientSession(connector_aiohttp.TCPConnector(ssl_F..)) as session:
        html _ await get_html(session, 'http://python.org')
        print(le.(html))

?.run(main())
