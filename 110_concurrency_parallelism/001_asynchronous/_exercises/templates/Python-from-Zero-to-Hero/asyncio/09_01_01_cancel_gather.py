____ threading
____ t___
_____ ____ ____ CancelledError, FIRST_EXCEPTION
____ ____
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
    print(f'{task_name=} sleeping')
    _____ ____.s..(sleeping_period)
    print(f'{task_name=} finished sleeping')

    print(f'Finished task={task_name}')
    return [Photo.from_json(photo) for photo in photos_json]


___ get_coros(session):
    return [
        photos_by_album('t1', 1, session),
        photos_by_album('t2', 2, session),
        photos_by_album('t3', 3, session),
        photos_by_album('t4', 4, session),
    ]


___ cancel_future(loop, future, after):
    ___ inner_cancel():
        print('sleeping before future cancel')
        t___.s..(after)
        print('cancel future')
        loop.call_soon_threadsafe(future.cancel)

    t = threading.Thread(target=inner_cancel)
    t.start()


___ cancel_tasks(tasks, after):
    ___ inner_cancel():
        t___.s..(after)
        for i, t in enumerate(tasks, start=1):
            print(f'cancel {i}, {t}')
            print(t.cancel())

    t = threading.Thread(target=inner_cancel)
    t.start()


_____ ___ main_gather_cancel_on_tasks():
    _____ with aiohttp.ClientSession() as session:
        tasks = [____.create_task(coro) for coro in get_coros(session)]
        future = ____.gather(*tasks)

        cancel_tasks(tasks, 2)

        try:
            print('awaiting future')
            result = _____ future
        except ____.exceptions.CancelledError as ex:
            print(f'Excepted at await {repr(ex)}')


_____ ___ main_gather_cancel_on_future():
    _____ with aiohttp.ClientSession() as session:
        future = ____.gather(*(get_coros(session)))

        cancel_future(____.get_running_loop(), future, 2)

        try:
            print('awaiting future')
            result = _____ future
        except ____.exceptions.CancelledError as ex:
            print(f'Excepted at await {repr(ex)}')


_____ ___ main_gather_return_exceptions():
    _____ with aiohttp.ClientSession() as session:
        tasks = [____.create_task(coro) for coro in get_coros(session)]
        future = ____.gather(*tasks, return_exceptions=True)

        cancel_tasks(tasks, 2)

        try:
            print('awaiting')
            results = _____ future
            for result in results:
                if isinstance(result, ____.exceptions.CancelledError):
                    print(repr(result))
                else:
                    print_photo_titles(result)
            print('after for')
        except ____.exceptions.CancelledError as ex:
            print(f'Excepted at await {repr(ex)}')


__ _______ __ _______
    loop = ____.get_event_loop()

    try:
        # loop.create_task(main_gather_cancel_on_future())
        # loop.create_task(main_gather_cancel_on_tasks())
        loop.create_task(main_gather_return_exceptions())
        loop.run_forever()
    finally:
        print('Closing loop')
        loop.close()
