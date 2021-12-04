____ ____
_____ ____ ____ FIRST_EXCEPTION

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
    print('print photo titles')
    for photo in photos:
        print(f'{photo.title}', end='\n')


_____ ___ photos_by_album(task_name, album, session):
    print(f'{task_name=}')
    if not isinstance(album, int):
        _____ ____.s..(2)
        raise RuntimeError('invalid album number')

    url = f'https://jsonplaceholder.typicode.com/albums/{album}/photos/'
    response = _____ session.get(url)
    photos_json = _____ response.json()

    sleeping_period = 3 if task_name == 't3' else 1
    _____ ____.s..(sleeping_period)

    print(f'Finished task={task_name}')
    return [Photo.from_json(photo) for photo in photos_json]


_____ ___ main_wait():
    _____ with aiohttp.ClientSession() as session:
        tasks = [
            photos_by_album('t1', 1, session),
            photos_by_album('t2', 2, session),
            photos_by_album('t3', 3, session),
            photos_by_album('ta', 'a', session),
            photos_by_album('t4', 4, session),
        ]

        photos = []
        # done_tasks, pending_tasks = await asyncio.wait(tasks)
        done_tasks, pending_tasks = _____ ____.wait(tasks, return_when=FIRST_EXCEPTION)

        for pending_task in pending_tasks:
            print(f'cancelling {pending_task}')
            print(pending_task.cancel())

        for done in done_tasks:
            try:
                result = done.result()
                photos.extend(result)
            except Exception as ex:
                print(repr(ex))

        print_photo_titles(photos)


__ _______ __ _______
    loop = ____.get_event_loop()

    try:
        loop.create_task(main_wait())
        loop.run_forever()
    finally:
        print('Closing loop')
        loop.close()
