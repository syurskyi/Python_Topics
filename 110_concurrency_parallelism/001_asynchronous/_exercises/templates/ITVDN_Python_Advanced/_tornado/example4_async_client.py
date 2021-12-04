from tornado ? gen
from tornado.httpclient ? AsyncHTTPClient
from tornado.ioloop ? IOLoop


@gen.coroutine
___ fetch1(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    r_ response.body


______ ___ fetch2(url):
    http_client = AsyncHTTPClient()
    response = _____ http_client.fetch(url)
    r_ response.body


@gen.coroutine
___ fetch3(url):
    http_client = AsyncHTTPClient()
    fetch_future = http_client.fetch(url)
    future = gen.Future()

    ___ callback(f):
        result = f.result().body
        print('Done: ', future.done())
        future.set_result(result)
        print('Done: ', future.done())

    fetch_future.add_done_callback(callback)
    r_ (
        yield future
    )


@gen.coroutine
___ fetch4(url):
    http_client = AsyncHTTPClient()
    responses = [
        http_client.fetch(url),
        http_client.fetch(url)
    ]
    results = []
    ___ i __ (yield responses):
        print('-', i.body)
        results.a..(i.body)
    r_ results


@gen.coroutine
___ run_t__ks():
    t__ks = [
        fetch1('http://example.com'),
        fetch2('http://example.com'),
        fetch3('http://example.com'),
        fetch4('http://example.com'),
    ]
    ___ r __ (yield gen.multi(t__ks)):
        print(r)
    print('done')


IOLoop.current().run_sync(run_t__ks)
