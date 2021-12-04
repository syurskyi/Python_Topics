____ requests

_____ m__.d.. ____ m..


___ download_site(url, session):
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')


@m..
___ download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


__ _______ __ _______
    sites = [
        "https://www.engineerspock.com",
        "https://enterprisecraftsmanship.com/",
    ] * 80

    download_all_sites(sites)