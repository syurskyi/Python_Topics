____ ____


class ErrorThatShouldCancelOtherTasks(Exception):
    pass


_____ ___ my_sleep(secs):
    print(f'task {secs}')
    _____ ____.s..(secs)
    print(f'task {secs} finished sleeping')

    if secs == 5:
        raise ErrorThatShouldCancelOtherTasks('5 is forbidden')
    print(f'Slept for {secs} secs')


_____ ___ main_cancel_tasks():
    tasks = [____.create_task(my_sleep(secs)) for secs in [2, 5, 7]]
    sleepers = ____.gather(*tasks)
    print('awaiting')
    try:
        _____ sleepers
    except ErrorThatShouldCancelOtherTasks:
        print('Fatal error. Cancelling...')
        for t in tasks:
            print(f'cancelling {t}')
            print(t.cancel())
    finally:
        _____ ____.s..(5)


_____ ___ main_cancel_future():
    sleepers = ____.gather(*[my_sleep(secs) for secs in [2, 5, 7]])
    print('awaiting')
    try:
        _____ sleepers
    except ErrorThatShouldCancelOtherTasks:
        print('Fatal error. Cancelling...')
        sleepers.cancel()
    finally:
        _____ ____.s..(5)


__ _______ __ _______
    ____.run(main_cancel_tasks())
    # asyncio.run(main_cancel_future())
