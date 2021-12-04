____ ____


c_ ErrorThatShouldCancelOtherTasks(Exception):
    pass


_____ ___ my_sleep(secs):
    print(f'task {secs}')
    _____ ____.s..(secs)
    print(f'task {secs} finished sleeping')

    __ secs == 5:
        raise ErrorThatShouldCancelOtherTasks('5 is forbidden')
    print(f'Slept for {secs} secs')


_____ ___ main_cancel_tasks():
    tasks = [____.create_task(my_sleep(secs)) ___ secs __ [2, 5, 7]]
    sleepers = ____.gather(*tasks)
    print('awaiting')
    ___
        _____ sleepers
    _______ ErrorThatShouldCancelOtherTasks:
        print('Fatal error. Cancelling...')
        ___ t __ tasks:
            print(f'cancelling {t}')
            print(t.cancel())
    _______
        _____ ____.s..(5)


_____ ___ main_cancel_future():
    sleepers = ____.gather(*[my_sleep(secs) ___ secs __ [2, 5, 7]])
    print('awaiting')
    ___
        _____ sleepers
    _______ ErrorThatShouldCancelOtherTasks:
        print('Fatal error. Cancelling...')
        sleepers.cancel()
    _______
        _____ ____.s..(5)


__ _______ __ _______
    ____.run(main_cancel_tasks())
    # asyncio.run(main_cancel_future())
