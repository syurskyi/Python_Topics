import hashlib
from concurrent.futures import ThreadPoolExecutor

import tornado.ioloop
import tornado.web
import tornado.gen

pool = ThreadPoolExecutor(5)


def sync_highload_task(password):
    for i in range(9876565):
        password = hashlib.sha256(password).hexdigest().encode()
    return password


@tornado.gen.coroutine
def make_password(password) -> str:
    hashed_password = yield pool.submit(
        sync_highload_task,
        password.encode()
    )
    return hashed_password


class IndexHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        value = self.get_query_argument('password', '')
        if value:
            hashed_password = yield make_password(value)
            self.write('<h1>Hashed password: {}</h1>'.format(
                hashed_password.decode())
            )
        self.write(
            '<form>'
            '<input type="text" name="password" placeholder="Password"/>'
            '<input type="submit"/>'
            '</form>'
        )


def make_app():
    url_handlers = [
        tornado.web.URLSpec(r'^/$', IndexHandler, name='index'),
    ]
    return tornado.web.Application(
        url_handlers,
        autoreload=True
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    print('started')
    tornado.ioloop.IOLoop.current().start()
