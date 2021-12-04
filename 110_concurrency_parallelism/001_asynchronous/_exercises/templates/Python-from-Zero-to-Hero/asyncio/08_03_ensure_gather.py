____ ____
____ t___

____ aiohttp


class Photo:
    ___ __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.thumbnailUrl = thumbnail_url
        self.url = url
        self.title = title
        self.photo_id = photo_id
        self.albumId = album_id

    @classmethod
    ___ from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


___ print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


_____ ___ photos_by_album(task_name, album, session):
    if not isinstance(album, int):
        raise RuntimeError('invalid album number')

    print(f'{task_name=}')
    url = f'https://jsonplaceholder.typicode.com/albums/{album}/photos/'
    response = _____ session.get(url)
    photos_json = _____ response.json()

    _____ ____.s..(1)
    return [Photo.from_json(photo) for photo in photos_json]


_____ ___ download_albums(albums):
    photos = []
    _____ with aiohttp.ClientSession() as session:
        for album in albums:
            photos.extend(_____ photos_by_album(f't{album}', album, session))
    return photos


_____ ___ main1():
    task1 = ____.create_task(download_albums([1, 2, 'a', 4]))

    try:
        result = _____ task1
    except Exception as ex:
        print(repr(ex))

    print('sleeping in main')
    _____ ____.s..(5)
    print('after sleep')


___ handle_result(fut):
    print(fut.result())


_____ ___ main2():
    task1 = ____.create_task(download_albums([1, 2, 'a', 4]))

    task1.add_done_callback(handle_result)

    print('sleeping in main')
    _____ ____.s..(5)
    print('after sleep')


_____ ___ main_gather():
    _____ with aiohttp.ClientSession() as session:
        tasks = [
            photos_by_album('t1', 1, session),
            photos_by_album('t2', 2, session),
            photos_by_album('ta', 'a', session),
            photos_by_album('t3', 3, session),
        ]

        photos = []
        results = _____ ____.gather(*tasks, return_exceptions=True)
        for res in results:
            if isinstance(res, Exception):
                print(repr(res))
            else:
                photos.extend(res)

        print_photo_titles(photos)


__ _______ __ _______
    ____.run(main_gather())

    t___.s..(3)
    print('main ended')
