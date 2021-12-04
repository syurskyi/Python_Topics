from tornado ? gen
from tornado.ioloop ? IOLoop
from tornado.locks ? Event

event = Event()


______ ___ consumer():
    print('Waiting for product')

    _____ event.wait()
    print('Product was found')
    event.clear()

    _____ event.wait()
    print('Product was found twice')

    r_ 1


______ ___ producer():
    print("About to set the event")

    _____ gen.sleep(5)
    print('Set Event')
    event.set()

    _____ gen.sleep(5)
    print('Set Event')
    event.set()

    r_ 2


______ ___ runner():
    results = _____ gen.multi([
        producer(),
        consumer()
    ])
    print(results)


IOLoop.current().run_sync(runner)
