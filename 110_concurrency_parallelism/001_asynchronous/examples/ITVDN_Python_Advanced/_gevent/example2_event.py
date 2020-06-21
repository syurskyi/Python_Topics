import gevent
from gevent.event import Event


def waiter():
    print('I am waiting for event')
    event.wait()
    print('Waiter done')


def emitter():
    print('Emitter is sleeping')
    gevent.sleep(3)
    event.set()
    print('I kill endless task!')
    endless_task.kill()


def endless():
    while True:
        print('Endless Task will be working forever!')
        gevent.sleep(2)


event = Event()

endless_task = gevent.spawn(endless)
jobs = [
    gevent.spawn(emitter),
    gevent.spawn(waiter),
    endless_task,
]

gevent.wait(jobs)
