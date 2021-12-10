______ aiohttp
______ _

@ ___ fetch_page(url):
    @ with aiohttp.ClientSession() as session:
        @ with session.get(url) as response:
            print(response.status)
            r.. response.status

loop = _.get_event_loop()
loop.run_until_complete(fetch_page('http://google.com'))