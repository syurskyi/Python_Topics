# ch10/example2.py

______ a..
______ ti..

? ___ count_down(name, delay):
    indents _ (or.(name) - or.('A')) * '\t'

    n _ 3
    w__ n:
        ? ?.s..(delay)

        duration _ t__.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n -_ 1

? ___ main():

    ? ?.gather(*[
        count_down('A', 1),
        count_down('B', 0.8),
        count_down('C', 0.5)
    ])

start _ t__.perf_counter()
?.run(main())

print('-' * 40)
print('Done.')
