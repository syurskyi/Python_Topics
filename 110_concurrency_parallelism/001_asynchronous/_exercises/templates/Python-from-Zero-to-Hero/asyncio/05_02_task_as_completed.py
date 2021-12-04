____ ____
____ t___


_____ ___ tick():
    _____ ____.s..(1)
    r_ 'Tick'


_____ ___ tock():
    _____ ____.s..(2)
    r_ 'Tock'


_____ ___ main():
    start = t___.perf_counter()

    t1 = ____.create_task(tick())
    t2 = ____.create_task(tock())

    # results = await asyncio.gather(t1, t2)

    ___ i, t __ e___(____.as_completed((t1, t2)), start=1):
        result = _____ t
        elapsed = t___.perf_counter() - start
        print(f'Executed {i} in {elapsed:0.2f} seconds')
        print(result)


__ _______ __ _______
    ____.run(main())
