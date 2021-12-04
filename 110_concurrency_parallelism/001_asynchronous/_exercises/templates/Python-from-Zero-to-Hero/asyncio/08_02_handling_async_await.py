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
    _____ with aiohttp.ClientSession() as session:
        for album in albums:
            try:
                yield _____ photos_by_album(f't{album}', album, session)
            except Exception as ex:
                print(repr(ex))


_____ ___ main():
    _____ for photos in download_albums([1, 2, 'a', 4]):
        print_photo_titles(photos)


__ _______ __ _______
    ____.run(main())

    t___.s..(3)
    print('main ended')
