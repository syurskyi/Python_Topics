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
    _____ w___ aiohttp.ClientSession() __ session:
        _____ w___ session.get(url) __ response:
            r_ _____ response.json()


_____ ___ fetch_ip(service):
    print(f'Fetching IP from {service.name}')

    json_response = _____ get_json(service.url)
    ip = json_response[service.ip_attr]
    r_ f'{service.name} finished with result: {ip}'


_____ ___ main():
    coros = [fetch_ip(service) ___ service __ services]

    done, pending = _____ ____.wait(coros, return_when=FIRST_COMPLETED)

    ___ x __ done:
        print(x.result())


__ _______ __ _______
    ____.run(main())
