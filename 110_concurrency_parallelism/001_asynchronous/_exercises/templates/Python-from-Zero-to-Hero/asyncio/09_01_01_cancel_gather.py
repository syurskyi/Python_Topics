____ __________
____ t___
_____ ____ ____ CancelledError, FIRST_EXCEPTION
____ ____
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
    print('print photo titles')
    ___ photo __ photos:
        print(f'{photo.title}', e.._'\n')


_____ ___ photos_by_album(task_name, album, session):
    print(f'{task_name=}')
    __ not isinstance(album, int):
        _____ ____.s..(2)
        r__ RuntimeError('invalid album number')

    url = f'https://jsonplaceholder.typicode.com/albums/{album}/photos/'

    response = _____ session.get(url)
    photos_json = _____ response.json()

    sleeping_period = 3 __ task_name == 't3' else 1
    print(f'{task_name=} sleeping')
    _____ ____.s..(sleeping_period)
    print(f'{task_name=} finished sleeping')

    print(f'Finished task={task_name}')
    r_ [Photo.from_json(photo) ___ photo __ photos_json]


___ get_coros(session):
    r_ [
        photos_by_album('t1', 1, session),
        photos_by_album('t2', 2, session),
        photos_by_album('t3', 3, session),
        photos_by_album('t4', 4, session),
    ]


___ cancel_future(loop, future, after):
    ___ inner_cancel
        print('sleeping before future cancel')
        t___.s..(after)
        print('cancel future')
        loop.call_soon_threadsafe(future.cancel)

    t = __________.T__(target=inner_cancel)
    t.start()


___ cancel_tasks(tasks, after):
    ___ inner_cancel
        t___.s..(after)
        ___ i, t __ e___(tasks, start=1):
            print(f'cancel {i}, {t}')
            print(t.cancel())

    t = __________.T__(target=inner_cancel)
    t.start()


_____ ___ main_gather_cancel_on_tasks
    _____ w___ aiohttp.ClientSession() __ session:
        tasks = [____.create_task(coro) ___ coro __ get_coros(session)]
        future = ____.gather(*tasks)

        cancel_tasks(tasks, 2)

        ___
            print('awaiting future')
            result = _____ future
        _______ ____.exceptions.CancelledError __ ex:
            print(f'Excepted at await {repr(ex)}')


_____ ___ main_gather_cancel_on_future
    _____ w___ aiohttp.ClientSession() __ session:
        future = ____.gather(*(get_coros(session)))

        cancel_future(____.get_running_loop(), future, 2)

        ___
            print('awaiting future')
            result = _____ future
        _______ ____.exceptions.CancelledError __ ex:
            print(f'Excepted at await {repr(ex)}')


_____ ___ main_gather_return_exceptions
    _____ w___ aiohttp.ClientSession() __ session:
        tasks = [____.create_task(coro) ___ coro __ get_coros(session)]
        future = ____.gather(*tasks, return_exceptions=True)

        cancel_tasks(tasks, 2)

        ___
            print('awaiting')
            results = _____ future
            ___ result __ results:
                __ isinstance(result, ____.exceptions.CancelledError):
                    print(repr(result))
                else:
                    print_photo_titles(result)
            print('after for')
        _______ ____.exceptions.CancelledError __ ex:
            print(f'Excepted at await {repr(ex)}')


__ _______ __ _______
    loop = ____.get_event_loop()

    ___
        # loop.create_task(main_gather_cancel_on_future())
        # loop.create_task(main_gather_cancel_on_tasks())
        loop.create_task(main_gather_return_exceptions())
        loop.run_forever()
    _______
        print('Closing loop')
        loop.close()
