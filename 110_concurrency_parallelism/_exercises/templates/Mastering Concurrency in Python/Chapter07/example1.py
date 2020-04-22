# ch7/example1.py

______ m..


c_ ReductionConsumer(?.P..):

    ___  - (self, task_queue, result_queue):
        ?.P... - (self)
        self.task_queue _ task_queue
        self.result_queue _ result_queue

    ___ run(self):
        pname _ self.name
        print('Using process %s...' % pname)

        w__ T..:
            num1 _ self.task_queue.g..
            __ num1 is N..:
                print('Exiting process %s.' % pname)
                self.task_queue.task_done()
                break

            self.task_queue.task_done()
            num2 _ self.task_queue.g..
            __ num2 is N..:
                print('Reaching the end with process %s and number %i.' % (pname, num1))
                self.task_queue.task_done()
                self.result_queue.put(num1)
                break

            print('Running process %s on numbers %i and %i.' % (pname, num1, num2))
            self.task_queue.task_done()
            self.result_queue.put(num1 + num2)


___ reduce_sum(array):
    tasks _ ?.JoinableQueue()
    results _ ?.JoinableQueue()
    result_size _ le.(array)

    n_consumers _ ?.cpu_count()

    ___ item __ array:
        results.put(item)

    w__ result_size > 1:
        tasks _ results
        results _ ?.JoinableQueue()

        consumers _ [ReductionConsumer(tasks, results) ___ i __ ra..(n_consumers)]
        ___ consumer __ consumers:
            consumer.s..

        ___ i __ ra..(n_consumers):
            tasks.put(N..)

        tasks.j..
        result_size _ result_size // 2 + (result_size % 2)
        #print('-' * 40)

    r_ results.g..


my_array _ [i ___ i __ ra..(20)]

result _ reduce_sum(my_array)
print('Final result: %i.' % result)
