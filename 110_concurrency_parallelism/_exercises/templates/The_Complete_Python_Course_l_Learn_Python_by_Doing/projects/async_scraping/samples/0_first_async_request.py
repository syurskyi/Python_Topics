______ aiohttp
______ asyncio

async ___ fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            return response.status

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_page('http://google.com'))