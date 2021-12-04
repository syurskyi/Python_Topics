____ requests

_____ m__.d.. ____ m..


___ download_site(url, session):
    w___ session.get(url) __ response:
        print(f'Read {len(response.content)} from {url}')


@m..
___ download_all_sites(sites):
    w___ requests.Session() __ session:
        ___ url __ sites:
            download_site(url, session)


__ _______ __ _______
    sites = [
        "https://www.engineerspock.com",
        "https://enterprisecraftsmanship.com/",
    ] * 80

    download_all_sites(sites)