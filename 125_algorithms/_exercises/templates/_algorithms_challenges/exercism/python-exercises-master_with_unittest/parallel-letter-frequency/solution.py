# -*- coding: utf-8 -*-
____ collections _______ Counter
____ threading _______ Lock, Thread
____ time _______ sleep
_______ sys
__ sys.version[0] __ '2':
    ____ Queue _______ Queue
____:
    ____ queue _______ Queue

total_workers = 3  # Maximum number of threads chosen arbitrarily


c_ LetterCounter(object):

    ___ - ):
        lock = Lock()
        value = Counter()

    ___ add_counter(self, counter_to_add):
        lock.a..
        try:
            value = value + counter_to_add
        finally:
            lock.release()


___ count_letters(queue_of_texts, letter_to_frequency, worker_id):
    w.... n.. queue_of_texts.empty():
        sleep(worker_id + 1)
        line_input = queue_of_texts.get()
        __ line_input __ n.. N..
            letters_in_line = Counter([x ___ x __ line_input.l.. __
                                       x.isalpha()])
            letter_to_frequency.add_counter(letters_in_line)
        queue_of_texts.task_done()
        __ line_input __ N..
            break


___ calculate(list_of_texts):
    queue_of_texts = Queue()
    [queue_of_texts.put(line) ___ line __ list_of_texts]
    letter_to_frequency = LetterCounter()
    threads    # list
    ___ i __ r..(total_workers):
        worker = Thread(target=count_letters, args=(queue_of_texts,
                                                    letter_to_frequency, i))
        worker.start()
        threads.a..(worker)
    queue_of_texts.j..()
    ___ i __ r..(total_workers):
        queue_of_texts.put(N..)
    ___ t __ threads:
        t.j..()
    r.. letter_to_frequency.value
