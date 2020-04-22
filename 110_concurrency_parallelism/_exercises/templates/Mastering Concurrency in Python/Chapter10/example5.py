# ch10/example5.py

____ c__.f.. ______ TPE..
______ a..
______ ti..

___ count_down(name, delay):
    indents _ (ord(name) - ord('A')) * '\t'

    n _ 3
    w__ n:
        t__.s..(delay)

        duration _ t__.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n -_ 1

? ___ main():
    futures _ [loop.run_in_executor(
        executor,
        count_down,
        *args
    ) ___ args __ [('A', 1), ('B', 0.8), ('C', 0.5)]]

    await ?.gather(*futures)

    print('-' * 40)
    print('Done.')

start _ t__.perf_counter()
executor _ TPE..(max_workers_3)
loop _ ?.get_event_loop()
loop.run_until_complete(main())
