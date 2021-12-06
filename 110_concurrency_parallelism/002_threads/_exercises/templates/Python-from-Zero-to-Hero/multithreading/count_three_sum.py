___ r...(path):
    lst = []
    w___ open(path, 'r') __ f:
        w.... line := f.readlineg___
            lst.a..(int(line))

    r_ lst


___ c..(ints, thread_name='t'):
    print(f'started count_three_sum in {thread_name}')

    n = l..(ints)
    counter = 0

    ___ i __ r..(n):
        ___ j __ r..(i + 1, n):
            ___ k __ r..(j + 1, n):
                __ ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found in {thread_name}:{ints[i]}, {ints[j]}, {ints[k]}', e.._'\n')

    print(f'ended count_three_sum in {thread_name}. Triplets counter={counter}')
    r_ counter
