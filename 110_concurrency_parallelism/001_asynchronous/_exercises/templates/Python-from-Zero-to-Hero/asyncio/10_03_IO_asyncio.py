____ ____

____ aiohttp
____ requests
____ t___

_____ m__.d.. ____ a..


_____ ___ download_site(url, session):
    _____ with session.get(url) as response:
        print(f"Read {response.content.total_bytes} from {url}")


@a..
_____ ___ download_all_sites(sites):
    _____ with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = ____.create_task(download_site(url, session))
            tasks.append(task)

        try:
            print('before await')
            _____ ____.gather(*tasks, return_exceptions=True)
        except Exception as ex:
            print(repr(ex))


if __name__ == "__main__":
    sites = [
                "https://www.engineerspock.com",
                "https://enterprisecraftsmanship.com/",
            ] * 80

    ____.run(download_all_sites(sites))

