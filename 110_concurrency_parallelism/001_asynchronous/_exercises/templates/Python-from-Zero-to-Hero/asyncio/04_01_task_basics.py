____ ____


_____ ___ tick():
    print("Tick")
    _____ ____.s..(1)
    print("Tock")
    r_ 'Tick-Tock'


_____ ___ main():
    t1 = ____.create_task(tick(), name='tick1')
    t2 = ____.ensure_future(tick())

    # await t1
    # await t2

    results = _____ ____.gather(t1, t2)

    print(f'{t1.get_name()}. Done = {t1.done()}')
    print(f'{t2.get_name()}. Done = {t2.done()}')

    ___ x __ results:
        print(x)


__ _______ __ _______
    ____.run(main())
