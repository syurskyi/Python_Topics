____ threading
____ concurrent.futures
____ requests

_____ m__.d.. ____ m..

thread_local = threading.local()


___ get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


___ download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')


@m..
___ download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


__ _______ __ _______
    sites = [
                "https://www.engineerspock.com",
                "https://enterprisecraftsmanship.com/",
            ] * 80

    download_all_sites(sites)
