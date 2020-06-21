from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Event

event = Event()


async def consumer():
    print('Waiting for product')

    await event.wait()
    print('Product was found')
    event.clear()

    await event.wait()
    print('Product was found twice')

    return 1


async def producer():
    print("About to set the event")

    await gen.sleep(5)
    print('Set Event')
    event.set()

    await gen.sleep(5)
    print('Set Event')
    event.set()

    return 2


async def runner():
    results = await gen.multi([
        producer(),
        consumer()
    ])
    print(results)


IOLoop.current().run_sync(runner)
