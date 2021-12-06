_______ _
_______ t___

____ _.c.. _______ r...


c_ ThreeSumTask:

    ___ __init__( ints):
        ints = ints
        canceled = False
        lock_obj = _.L..

    ___ run(self):
        c..(ints)

    ___ cancel(self):
        w___ lock_obj:
            canceled = True

    ___ c..( ints):
        print(f'started count_three_sum')

        n = len(ints)
        counter = 0

        ___ i __ r..(n):
            ___ j __ r..(i + 1, n):
                ___ k __ r..(j + 1, n):
                    __ canceled:
                        print('Task was Cancelled')
                        counter = -1
                        r_ counter

                    __ ints[i] + ints[j] + ints[k] == 0:
                        counter += 1
                        print(f'Triple found:{ints[i]}, {ints[j]}, {ints[k]}', e.._'\n')

        print(f'ended count_three_sum. Triplets counter={counter}')
        r_ counter


__ _____ __ _____
    print('started main')

    ints = r...('..\\data\\1Kints.txt')

    task = ThreeSumTask(ints)
    t1 = _.T..(t.._task.run)
    t1.s..

    t___.s(5)

    task.cancel()

    t1.j...

    print('ended main')
