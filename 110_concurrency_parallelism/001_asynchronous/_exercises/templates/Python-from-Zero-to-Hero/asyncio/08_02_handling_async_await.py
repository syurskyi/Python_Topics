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
        raise RuntimeError('invalid album number')

    print(f'{task_name=}')
    url = f'https://jsonplaceholder.typicode.com/albums/{album}/photos/'
    response = _____ session.get(url)
    photos_json = _____ response.json()

    _____ ____.s..(1)
    r_ [Photo.from_json(photo) ___ photo __ photos_json]


_____ ___ download_albums(albums):
    _____ w___ aiohttp.ClientSession() __ session:
        ___ album __ albums:
            ___
                yield _____ photos_by_album(f't{album}', album, session)
            _______ Exception __ ex:
                print(repr(ex))


_____ ___ main():
    _____ ___ photos __ download_albums([1, 2, 'a', 4]):
        print_photo_titles(photos)


__ _______ __ _______
    ____.run(main())

    t___.s..(3)
    print('main ended')
