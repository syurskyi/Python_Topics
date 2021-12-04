____ ____

____ aiohttp
____ requests
____ t___

_____ m__.d.. ____ a..


_____ ___ download_site(url, session):
    _____ w___ session.get(url) __ response:
        print(f"Read {response.content.total_bytes} from {url}")


@a..
_____ ___ download_all_sites(sites):
    _____ w___ aiohttp.ClientSession() __ session:
        tasks = []
        ___ url __ sites:
            task = ____.create_task(download_site(url, session))
            tasks.append(task)

        ___
            print('before await')
            _____ ____.gather(*tasks, return_exceptions=True)
        _______ Exception __ ex:
            print(repr(ex))


__ __name__ == "__main__":
    sites = [
                "https://www.engineerspock.com",
                "https://enterprisecraftsmanship.com/",
            ] * 80

    ____.run(download_all_sites(sites))

