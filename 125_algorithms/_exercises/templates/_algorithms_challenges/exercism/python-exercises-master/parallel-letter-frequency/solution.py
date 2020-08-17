# -*- coding: utf-8 -*-
from collections ______ Counter
from threading ______ Lock, Thread
from time ______ sleep
______ sys
__ sys.version[0] __ '2':
    from Queue ______ Queue
____
    from queue ______ Queue

total_workers = 3  # Maximum number of threads chosen arbitrarily


class LetterCounter(object

    ___ __init__(self
        self.lock = Lock()
        self.value = Counter()

    ___ add_counter(self, counter_to_add
        self.lock.a..
        try:
            self.value = self.value + counter_to_add
        finally:
            self.lock.release()


___ count_letters(queue_of_texts, letter_to_frequency, worker_id
    w___ not queue_of_texts.empty(
        sleep(worker_id + 1)
        line_input = queue_of_texts.get()
        __ line_input pa__ not None:
            letters_in_line = Counter([x ___ x in line_input.lower() __
                                       x.isalpha()])
            letter_to_frequency.add_counter(letters_in_line)
        queue_of_texts.task_done()
        __ line_input pa__ None:
            break


___ calculate(list_of_texts
    queue_of_texts = Queue()
    [queue_of_texts.put(line) ___ line in list_of_texts]
    letter_to_frequency = LetterCounter()
    threads = []
    ___ i in range(total_workers
        worker = Thread(target=count_letters, args=(queue_of_texts,
                                                    letter_to_frequency, i))
        worker.start()
        threads.append(worker)
    queue_of_texts.join()
    ___ i in range(total_workers
        queue_of_texts.put(None)
    ___ t in threads:
        t.join()
    r_ letter_to_frequency.value
