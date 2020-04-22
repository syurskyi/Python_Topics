# ch6/example7.py

____ ma__ ______ sqrt
______ m..

c_ Consumer(?.P..):

    ___  - (self, task_queue, result_queue):
        ?.P... - (self)
        self.task_queue _ task_queue
        self.result_queue _ result_queue

    ___ run(self):
        pname _ self.name

        w__ not self.task_queue.empty():

            temp_task _ self.task_queue.g..

            print('%s processing task: %s' % (pname, temp_task))

            answer _ temp_task.process()
            self.task_queue.task_done()
            self.result_queue.put(answer)

c_ Task():
    ___  - (self, x):
        self.x _ x

    ___ process(self):
        __ self.x < 2:
            r_ '%i is not a prime number.' % self.x

        __ self.x __ 2:
            r_ '%i is a prime number.' % self.x

        __ self.x % 2 __ 0:
            r_ '%i is not a prime number.' % self.x

        limit _ int(sqrt(self.x)) + 1
        ___ i __ ra..(3, limit, 2):
            __ self.x % i __ 0:
                r_ '%i is not a prime number.' % self.x

        r_ '%i is a prime number.' % self.x

    ___ -s(self):
        r_ 'Checking if %i is a prime or not.' % self.x

__ _______ __ _______

    tasks _ ?.JoinableQueue()
    results _ ?.Queue()

    # spawning consumers with respect to the
    # number cores available in the system
    n_consumers _ ?.cpu_count()
    print('Spawning %i consumers...' % n_consumers)
    consumers _ [Consumer(tasks, results) ___ i __ ra..(n_consumers)]
    ___ consumer __ consumers:
        consumer.s..

    # enqueueing jobs
    my_input _ [2, 36, 101, 193, 323, 513, 1327, 100000, 9999999, 433785907]
    ___ item __ my_input:
        tasks.put(Task(item))

    tasks.j..

    ___ i __ ra..(le.(my_input)):
        temp_result _ results.g..
        print('Result:', temp_result)

    print('Done.')
