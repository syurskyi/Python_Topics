______ aiohttp
______ _

@ ___ fetch_page(url):
    @ w__ aiohttp.ClientSession() __ session:
        @ w__ session.get(url) __ response:
            print(response.status)
            r.. response.status

loop = _.get_event_loop()
loop.run_until_complete(fetch_page('http://google.com'))