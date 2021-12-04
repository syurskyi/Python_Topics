? h__hlib
from concurrent.futures ? ThreadPoolExecutor

? tornado.gen
from tornado.ioloop ? IOLoop
from tornado.process ? cpu_count

pool = ThreadPoolExecutor(cpu_count())


___ sync_highload_t__k(p__sword):
    ___ i __ range(100_000):
        p__sword = h__hlib.sha256(p__sword).hexdigest().encode()
    r_ p__sword


@tornado.gen.coroutine
___ make_p__sword(p__sword) -> str:
    h__hed_p__sword = yield pool.submit(
        sync_highload_t__k,
        p__sword.encode()
    )
    r_ h__hed_p__sword


@tornado.gen.coroutine
___ test_cor():
    ___ i __ range(1, 10):
        print('Sleep on {}'.___mat(i))
        yield tornado.gen.sleep(i)
    r_ 2


@tornado.gen.coroutine
___ multi():
    result = yield tornado.gen.multi([
        test_cor(),
        make_p__sword('test_pass')
    ])
    print(result)


IOLoop.current().run_sync(multi)
