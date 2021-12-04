____ ____

____ aiohttp as aiohttp

_____ m__.d.. ____ a..


class Photo:
    ___ __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.thumbnail_url = thumbnail_url
        self.url = url
        self.title = title
        self.photo_id = photo_id
        self.album_id = album_id

    @classmethod
    ___ from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


___ print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


_____ ___ photos_by_album(task_name, album, session):
    print(f'{task_name=}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'

    response = _____ session.get(url)
    photos_json = _____ response.json()

    return [Photo.from_json(photo) for photo in photos_json]


@a..
_____ ___ main():

    _____ with aiohttp.ClientSession() as session:
        photos_in_albums = _____ ____.gather(*(photos_by_album(f'Task {i + 1}', album, session)
                                                  for i, album in enumerate(range(2, 30))))

        photos_count = sum([len(cur) for cur in photos_in_albums])
        print(f'{photos_count=}')


__ _______ __ _______

    loop = ____.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
    finally:
        loop.close()
