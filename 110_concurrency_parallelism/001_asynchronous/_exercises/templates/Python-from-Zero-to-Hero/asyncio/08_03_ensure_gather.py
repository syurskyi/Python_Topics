____ ____
____ t___

____ aiohttp


c_ Photo:
    ___  -   album_id, photo_id, title, url, thumbnail_url):
        thumbnailUrl = thumbnail_url
        url = url
        title = title
        photo_id = photo_id
        albumId = album_id

    @classmethod
    ___ from_json(cls, obj):
        r_ Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


___ print_photo_titles(photos):
    ___ photo __ photos:
        print(f'{photo.title}', e.._'\n')


_____ ___ photos_by_album(task_name, album, session):
    __ not isinstance(album, int):
        r__ RuntimeError('invalid album number')

    print(f'{task_name=}')
    url = f'https://jsonplaceholder.typicode.com/albums/{album}/photos/'
    response = _____ session.get(url)
    photos_json = _____ response.json()

    _____ ____.s..(1)
    r_ [Photo.from_json(photo) ___ photo __ photos_json]


_____ ___ download_albums(albums):
    photos = []
    _____ w___ aiohttp.ClientSession() __ session:
        ___ album __ albums:
            photos.extend(_____ photos_by_album(f't{album}', album, session))
    r_ photos


_____ ___ main1
    task1 = ____.create_task(download_albums([1, 2, 'a', 4]))

    ___
        result = _____ task1
    _______ Exception __ ex:
        print(repr(ex))

    print('sleeping in main')
    _____ ____.s..(5)
    print('after sleep')


___ handle_result(fut):
    print(fut.result())


_____ ___ main2
    task1 = ____.create_task(download_albums([1, 2, 'a', 4]))

    task1.add_done_callback(handle_result)

    print('sleeping in main')
    _____ ____.s..(5)
    print('after sleep')


_____ ___ main_gather
    _____ w___ aiohttp.ClientSession() __ session:
        tasks = [
            photos_by_album('t1', 1, session),
            photos_by_album('t2', 2, session),
            photos_by_album('ta', 'a', session),
            photos_by_album('t3', 3, session),
        ]

        photos = []
        results = _____ ____.gather(*tasks, return_exceptions=True)
        ___ res __ results:
            __ isinstance(res, Exception):
                print(repr(res))
            else:
                photos.extend(res)

        print_photo_titles(photos)


__ _______ __ _______
    ____.run(main_gather())

    t___.s..(3)
    print('main ended')
