import gevent


def task():
    print('Gevent sleep')
    gevent.sleep(1)
    print('Gevent finished')


jobs = [
    gevent.spawn(task),
    gevent.spawn(task),
    gevent.spawn(task)
]

gevent.joinall(jobs)
