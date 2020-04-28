#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 3.5.2.
# It may run on any other version with/without modifications.

______ ?
______ t__
______ datetime

______ tornado.httpserver
______ tornado.ioloop
______ tornado.options
______ tornado.web

____ tornado ______ gen
____ tornado.concurrent ______ return_future

c_ AsyncUser(o..):
    @return_future
    ___ req1 callback_None):
        t__.sleep(0.1)
        result _ datetime.datetime.utcnow()
        callback(result)

    @return_future
    ___ req2 callback_None):
        t__.sleep(0.2)
        result _ datetime.datetime.utcnow()
        callback(result)



c_ Application(tornado.web.Application):
    ___ -
        handlers _ [
            (r"/", UserHandler),
        ]
        tornado.web.Application.-  handlers)


c_ UserHandler(tornado.web.RequestHandler):
    @gen.coroutine
    ___ get
        user _ AsyncUser()
        response1 _ yield (user.req1())
        response2 _ yield (user.req2())
        print ("response1,2: @ @" (response1, response2))
        finish()

___ main(port):
    http_server _ tornado.httpserver.HTTPServer(Application())
    print("Server listening at Port: ", port)
    http_server.l..(port)
    tornado.ioloop.IOLoop.instance().s..


__ _____ __ ______
    parser _ ?.AP..(d.._'Async Server Example')
    parser.a_a..('--port', a.._"store", d.._"port", ty.._in., r.._T..)
    given_args _ parser.p_a..
    port _ given_args.port
    main(port)
