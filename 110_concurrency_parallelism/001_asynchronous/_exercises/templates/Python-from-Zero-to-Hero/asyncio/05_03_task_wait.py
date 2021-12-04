____ ____
_____ ____ ____ FIRST_COMPLETED
_____ collections ____ namedtuple

____ aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

services = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


_____ ___ get_json(url):
    _____ with aiohttp.ClientSession() as session:
        _____ with session.get(url) as response:
            return _____ response.json()


_____ ___ fetch_ip(service):
    print(f'Fetching IP from {service.name}')

    json_response = _____ get_json(service.url)
    ip = json_response[service.ip_attr]
    return f'{service.name} finished with result: {ip}'


_____ ___ main():
    coros = [fetch_ip(service) for service in services]

    done, pending = _____ ____.wait(coros, return_when=FIRST_COMPLETED)

    for x in done:
        print(x.result())


__ _______ __ _______
    ____.run(main())
