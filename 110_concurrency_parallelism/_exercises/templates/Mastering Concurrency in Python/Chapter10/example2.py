# ch10/example2.py

______ a..
______ ti..

? ___ count_down(name, delay):
    indents _ (ord(name) - ord('A')) * '\t'

    n _ 3
    w__ n:
        ? ?.s..(delay)

        duration _ t__.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n -_ 1

loop _ ?.g_e_l..
tasks _ [
    loop.create_task(count_down('A', 1)),
    loop.create_task(count_down('B', 0.8)),
    loop.create_task(count_down('C', 0.5))
]

start _ t__.perf_counter()
loop.r_u_c..(?.wait(tasks))

print('-' * 40)
print('Done.')
