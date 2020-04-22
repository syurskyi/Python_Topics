# ch10/example1.py

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

start _ t__.perf_counter()

count_down('A', 1)
count_down('B', 0.8)
count_down('C', 0.5)

print('-' * 40)
print('Done.')
