____ ____
_____ ____ ____ FIRST_EXCEPTION

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
        raise RuntimeError('invalid album number')

    url = f'https://jsonplaceholder.typicode.com/albums/{album}/photos/'
    response = _____ session.get(url)
    photos_json = _____ response.json()

    sleeping_period = 3 __ task_name == 't3' else 1
    _____ ____.s..(sleeping_period)

    print(f'Finished task={task_name}')
    r_ [Photo.from_json(photo) ___ photo __ photos_json]


_____ ___ main_wait
    _____ w___ aiohttp.ClientSession() __ session:
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

        ___ pending_task __ pending_tasks:
            print(f'cancelling {pending_task}')
            print(pending_task.cancel())

        ___ done __ done_tasks:
            ___
                result = done.result()
                photos.extend(result)
            _______ Exception __ ex:
                print(repr(ex))

        print_photo_titles(photos)


__ _______ __ _______
    loop = ____.get_event_loop()

    ___
        loop.create_task(main_wait())
        loop.run_forever()
    _______
        print('Closing loop')
        loop.close()
