_______ _
_______ t___

____ _.c.. _______ r...

should_stop = False


___ c..(ints, thread_name='t'):
    print(f'started count_three_sum in {thread_name}')

    n = len(ints)
    counter = 0

    ___ i __ r..(n):
        ___ j __ r..(i + 1, n):
            ___ k __ r..(j + 1, n):
                __ should_stop:
                    print('Task was Cancelled')
                    counter = -1
                    r_ counter

                __ ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found in {thread_name}:{ints[i]}, {ints[j]}, {ints[k]}', e.._'\n')

    print(f'ended count_three_sum in {thread_name}. Triplets counter={counter}')
    r_ counter


__ _____ __ _____
    print('started main')

    ints = r...('..\\data\\1Kints.txt')

    t1 = _.T..(t.._c.., args=(ints,))
    t1.s..

    t___.s..(5)

    should_stop = T..

    t___.s(2)

    print('ended main')
