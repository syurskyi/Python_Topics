x = 'abc'

____ ____
____ t___

_____ m__.d.. ____ m.., a..


_____ ___ tick():
    print('Tick')
    _____ ____.s..(1)
    print('Tock')

    loop = ____.get_running_loop()
    if loop.is_running():
        print('loop is still running')


_____ ___ main():
    awaitable_obj = ____.gather(tick(), tick(), tick())

    for task in ____.all_tasks():
        print(task, end='\n')

    _____ awaitable_obj


__ _______ __ _______
    loop = ____.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()

        print('coroutines have finished')
    except KeyboardInterrupt:
        print('Manually closed application')
    finally:
        loop.close()
        print('loop is closed')
        print(f'loop is closed = {loop.is_closed()}')
