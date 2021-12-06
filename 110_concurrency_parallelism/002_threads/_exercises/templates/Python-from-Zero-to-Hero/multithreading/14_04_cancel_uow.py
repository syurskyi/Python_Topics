_______ _
_______ t___

____ _.c.. _______ r...


c_ StoppableThread(_.T..):
    ___ - ( *args, **kwargs):
        super(StoppableThread, self).- (*args, **kwargs)
        stop_event = _.Event()

    ___ stop
        stop_event.set()

    ___ stopped
        r_ stop_event.is_set()


c_ ThreeSumUnitOfWork(StoppableThread):

    ___ - ( ints, name='TestThread'):
        super().- (name=name)
        ints = ints
        # self.stop_event = threading.Event()

    ___ run
        print(f'{getName()} starts')

        c..(ints)

        print(f'{getName()} ends')

    # def stop
    #     self.stop_event.set()

    ___ c..( ints):
        print(f'started count_three_sum')

        n = len(ints)
        counter = 0

        ___ i __ r..(n):
            ___ j __ r..(i + 1, n):
                ___ k __ r..(j + 1, n):
                    __ super().stoppedg___
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

    task = ThreeSumUnitOfWork(ints)
    task.s..

    t___.s(10)

    task.stop()

    task.j...

    print(task.stopped())
    print('ended main')
