# -*- coding: utf-8 -*-

# producer-consumer-coroutines

# """
# Сопрограмма (англ. coroutine) — компонент программы, обобщающий понятие
# подпрограммы, который дополнительно поддерживает множество входных точек
# (а не одну, как подпрограмма) и остановку и продолжение выполнения с
# сохранением определённого положения.

# Rolling our own Next method

class Squares:
    def __init__(self):
        self.i = 0

    def next_(self):
        result = self.i ** 2
        self.i += 1
        return result

sq = Squares()
sq.next_()
sq.next_()

for i in range(10):
    print(sq.next_())

# Coroutines
# The word co actually comes from cooperative.
# A coroutine is a generalization of subroutines (think functions), focused on cooperation between routines.
# If you have some concepts of multi-threading, this is similar in some ways.
# But whereas in multi-threaded applications the operating system usually decides when to suspend one thread and
# resume another, without asking permission, so-called preemptive multitasking,
# here we have routines that voluntarily yield control to something else - hence the term cooperative.

# Coroutines
#
# We can specify a maximum size for the queue when create it - this allows us to limit the number of items in the queue.
#
# (Note that I'm avoiding calling it the start and end of the queue,
# because what you consider the start/end of the queue might depend on how you are using it)

from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq

dq.append(100)
dq

dq.appendleft(-10)
dq

dq.pop()
dq
dq.popleft()

# Coroutines
#
# We can create a capped queue:
#
# As you can see the first item (2) was automatically discarded from the left of the queue when we added 300 to the right.
#
# We can also find the number of elements in the queue by using the len() function:
# as well as query the maxlen:

from collections import deque
dq = deque([1, 2, 3, 4], maxlen=5)
dq.append(100)
dq
dq.append(200)
dq
dq.append(300)
dq

len(dq)
dq.maxlen

# Coroutines
# Now let's create an empty queue, and write two functions - one that will add elements to the queue, and one that will consume elements from the queue:

def produce_elements(dq):
    for i in range(1, 36):
        dq.appendleft(i)

def consume_elements(dq):
    while len(dq) > 0:
        item = dq.pop()
        print('processing item', item)

def coordinator():
    dq = deque()
    producer = produce_elements(dq)
    consume_elements(dq)

coordinator()

# Coroutines
# The goal is to process these after some time, and not wait until all the items have been added to the queue -
# maybe the incoming stream is infinite even.
# In that case, we want to "pause" adding elements to the queue, process (consume) those items,
# then once they've all been processed we want to resume adding elements, and rinse and repeat.
# We'll use a capped deque, and change our producer and consumers slightly, so that each one does it's work,
# the yields control back to the caller once it's done with its work - the producer adding elements to the queue,
# and the consumer removing and processing elements from the queue:

def produce_elements(dq, n):
    for i in range(1, n):
        dq.appendleft(i)
        if len(dq) == dq.maxlen:
            print('queue full - yielding control')
            yield


def consume_elements(dq):
    while True:
        while len(dq) > 0:
            print('processing ', dq.pop())
        print('queue empty - yielding control')
        yield


def coordinator():
    dq = deque(maxlen=10)
    producer = produce_elements(dq, 36)
    consumer = consume_elements(dq)
    while True:
        try:
            print('producing...')
            next(producer)
        except StopIteration:
            # producer finished
            break
        finally:
            print('consuming...')
            next(consumer)


coordinator()


