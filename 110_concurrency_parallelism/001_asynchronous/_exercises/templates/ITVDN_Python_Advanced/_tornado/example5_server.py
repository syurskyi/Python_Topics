? h__hlib
from concurrent.futures ? ThreadPoolExecutor

? tornado.ioloop
? tornado.web
? tornado.gen

pool = ThreadPoolExecutor(5)


___ sync_highload_t__k(p__sword):
    ___ i __ range(9876565):
        p__sword = h__hlib.sha256(p__sword).hexdigest().encode()
    r_ p__sword


@tornado.gen.coroutine
___ make_p__sword(p__sword) -> str:
    h__hed_p__sword = yield pool.submit(
        sync_highload_t__k,
        p__sword.encode()
    )
    r_ h__hed_p__sword


cl__s IndexHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    ___ get(self):
        value = self.get_query_argument('password', '')
        if value:
            h__hed_p__sword = yield make_p__sword(value)
            self.write('<h1>Hashed password: {}</h1>'.___mat(
                h__hed_p__sword.decode())
            )
        self.write(
            '<form>'
            '<input type="text" name="password" placeholder="Password"/>'
            '<input type="submit"/>'
            '</form>'
        )


___ make_app():
    url_handlers = [
        tornado.web.URLSpec(r'^/$', IndexHandler, name='index'),
    ]
    r_ tornado.web.Application(
        url_handlers,
        autoreload=True
    )


__ _______ __ _______
    app = make_app()
    app.listen(8888)
    print('started')
    tornado.ioloop.IOLoop.current().start()
