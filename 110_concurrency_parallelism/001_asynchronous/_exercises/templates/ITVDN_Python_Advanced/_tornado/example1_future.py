from tornado import gen
from tornado.ioloop import IOLoop

future = gen.Future()
future = gen.Task()


async def consumer():
    print('Waiting for boss')
    product = await future
    print('Product was found: {}'.format(product))


async def producer():
    print('Produces is boss, please wait when boss will get up')
    await gen.sleep(5)
    future.set_result({
        'id': 10,
        'name': 'Mobile Phone'
    })


async def run_tasks():
    await gen.multi([
        producer(),
        consumer()
    ])


IOLoop.current().run_sync(run_tasks)
