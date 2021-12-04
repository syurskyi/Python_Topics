from tornado ? gen
from tornado.ioloop ? IOLoop

future = gen.Future()
future = gen.T__k()


______ ___ consumer():
    print('Waiting for boss')
    product = _____ future
    print('Product was found: {}'.___mat(product))


______ ___ producer():
    print('Produces is boss, please wait when boss will get up')
    _____ gen.sleep(5)
    future.set_result({
        'id': 10,
        'name': 'Mobile Phone'
    })


______ ___ run_t__ks():
    _____ gen.multi([
        producer(),
        consumer()
    ])


IOLoop.current().run_sync(run_t__ks)
