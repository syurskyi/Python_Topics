#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ ?
______ tornado.ioloop
______ tornado.httpclient


c_ TornadoAsync
    ___ handle_requestresponse):
        __ response.e..:
            print ("Error:", response.e..)
        ____
            print (response.body)
        tornado.ioloop.IOLoop.instance().stop()

___ run_server(url):
    tornadoAsync _ TornadoAsync()
    http_client _ tornado.httpclient.AsyncHTTPClient()
    http_client.fetch(url, tornadoAsync.handle_request)
    tornado.ioloop.IOLoop.instance().s..

__ _______ __ ______
    parser _ ?.AP..(d.._'Async Server Example')
    parser.a_a..('--url', a.._"store", d.._"url", type_str, r.._T..)
    given_args _ parser.p_a..
    url _ ?.url
    run_server(url)
